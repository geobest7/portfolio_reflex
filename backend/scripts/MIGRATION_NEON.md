# Migración PostgreSQL: Render → Neon

## Requisitos previos

- **PostgreSQL client tools** instalados (`pg_dump`, `psql`)
  - Windows: Instalar desde https://www.postgresql.org/download/windows/
  - O usar: `winget install PostgreSQL.PostgreSQL`
  - Solo necesitas las "Command Line Tools" en el instalador
- Credenciales de la DB actual en Render
- Cuenta en Neon (https://neon.tech)

---

## Paso 1: Obtener credenciales de Render

1. Ir a https://dashboard.render.com
2. Click en tu servicio de **PostgreSQL** (no el web service)
3. En la pestaña **Info**, copiar:
   - **External Database URL** (formato: `postgres://user:pass@host/dbname`)
   - Necesitas la URL **External** (no Internal)

---

## Paso 2: Crear base de datos en Neon

1. Ir a https://console.neon.tech
2. **Sign Up** (gratis, con GitHub o email)
3. Click **"New Project"**
   - **Name**: `portfolio-api`
   - **Region**: `eu-central-1` (Frankfurt) — más cercano a España
   - **PostgreSQL version**: 16 (o la más reciente disponible)
4. Una vez creado, ir a **Dashboard** → **Connection Details**
5. Copiar el **Connection string** (formato: `postgresql://user:pass@ep-xxx.eu-central-1.aws.neon.tech/neondb?sslmode=require`)

> **IMPORTANTE**: Guarda esta URL, la necesitarás en los pasos 4 y 6.

---

## Paso 3: Backup de la base de datos de Render

Abrir terminal (PowerShell o CMD) y ejecutar:

```bash
# Reemplazar RENDER_EXTERNAL_URL con tu URL externa de Render
# Ejemplo: postgres://user_abc:pass_xyz@dpg-xxx.frankfurt-postgres.render.com/portfolio_db

pg_dump "RENDER_EXTERNAL_URL" --no-owner --no-privileges --clean --if-exists -F p -f render_backup.sql
```

**Explicación de flags:**
- `--no-owner`: No incluir propietarios (diferentes entre Render y Neon)
- `--no-privileges`: No incluir permisos (diferentes entre proveedores)
- `--clean --if-exists`: DROP antes de CREATE (idempotente, seguro para re-ejecutar)
- `-F p`: Formato plain text SQL (legible y debuggeable)
- `-f render_backup.sql`: Archivo de salida

**Verificar el backup:**
```bash
# Ver tamaño del archivo
dir render_backup.sql

# Ver primeras líneas para confirmar que tiene contenido
type render_backup.sql | more
```

El archivo debe contener sentencias `CREATE TABLE`, `INSERT INTO`, etc.

---

## Paso 4: Importar en Neon

```bash
# Reemplazar NEON_URL con tu connection string de Neon
# Ejemplo: postgresql://user:pass@ep-xxx.eu-central-1.aws.neon.tech/neondb?sslmode=require

psql "NEON_URL" -f render_backup.sql
```

> **Nota**: Puede mostrar algunos warnings como `NOTICE: table "xxx" does not exist, skipping`.
> Esto es normal por los `DROP IF EXISTS` del backup. Los errores reales serán `ERROR:`.

**Si hay errores de SSL:**
```bash
# Añadir sslmode explícito si no está en la URL
psql "postgresql://user:pass@ep-xxx.neon.tech/neondb?sslmode=require" -f render_backup.sql
```

---

## Paso 5: Verificar la migración

Ejecutar el script de verificación contra Neon:

```bash
cd backend
set DATABASE_URL=postgresql://user:pass@ep-xxx.neon.tech/neondb?sslmode=require
python -m scripts.verify_db
```

**Output esperado:**
```
===========================================================
  VERIFICACIÓN DE BASE DE DATOS
===========================================================

--- 1. Conexión ---
  ✓ Conexión exitosa

--- 2. Tablas ---
  ✓ cursos
  ✓ experiencias
  ✓ github_repos
  ✓ proyectos
  ✓ users
  ✓ visitas

--- 3. Registros por tabla ---
  cursos: X registros
  experiencias: X registros
  ...

--- 5. Usuario admin ---
  ✓ Admin encontrado: ...
```

**Verificar que los conteos coincidan con Render** — ejecuta el mismo script contra la URL de Render para comparar.

---

## Paso 6: Actualizar DATABASE_URL en Render

1. Ir a https://dashboard.render.com
2. Click en tu **Web Service** (portfolio-api, NO el PostgreSQL)
3. Ir a **Environment** → **Environment Variables**
4. Editar `DATABASE_URL`:
   - **Valor anterior**: `postgres://...render.com/...` (Render PostgreSQL)
   - **Valor nuevo**: `postgresql://user:pass@ep-xxx.eu-central-1.aws.neon.tech/neondb?sslmode=require` (Neon)
5. Click **Save Changes**
6. Render hará **redeploy automático**

> **ROLLBACK**: Si algo falla, simplemente vuelve a poner la URL anterior de Render en esta misma variable.

---

## Paso 7: Verificar post-migración

1. **Esperar a que Render termine el redeploy** (~2-3 minutos)

2. **Test health endpoint:**
   ```bash
   curl https://portfolio-reflex-pwdv.onrender.com/health
   ```
   Debe retornar: `{"status": "healthy", "database": "connected"}`

3. **Test frontend:**
   - Ir a https://portfolio-alessandro-teal-moon.reflex.run
   - Verificar que cargan proyectos, cursos, experiencias
   - Verificar que funciona el login admin
   - Verificar que las analíticas se registran

4. **Test API directa:**
   ```bash
   curl https://portfolio-reflex-pwdv.onrender.com/api/proyectos/
   curl https://portfolio-reflex-pwdv.onrender.com/api/cursos/
   curl https://portfolio-reflex-pwdv.onrender.com/api/experiencias/
   ```

---

## Paso 8: Limpieza (después de verificar que todo funciona)

- **No borrar** la DB de Render inmediatamente — déjala como backup hasta que expire el 8 de marzo
- El archivo `render_backup.sql` es tu backup offline — guárdalo en un lugar seguro

---

## Neon: Plan gratuito — Límites

| Recurso | Límite gratuito |
|---------|----------------|
| **Storage** | 0.5 GB |
| **Compute** | 191 horas/mes (se suspende tras inactividad, se reactiva automáticamente) |
| **Branches** | 10 |
| **Projects** | 1 |

> **Diferencia con Render**: Neon es serverless — la DB se "suspende" tras inactividad pero **se reactiva automáticamente** en ~500ms con la primera query. No necesita ping manual. El backend con `pool_pre_ping=True` maneja esto transparentemente.

---

## Troubleshooting

### Error: "SSL connection is required"
→ Asegúrate de que la URL tiene `?sslmode=require` al final

### Error: "connection refused" desde psql
→ Verificar que la URL es correcta y que el proyecto Neon está activo

### Error: "permission denied for table"
→ Usar `--no-owner --no-privileges` en pg_dump

### Los datos no aparecen en el frontend
→ Verificar con `curl` que la API retorna datos. Si retorna [], el import falló — re-ejecutar paso 4

### El backend no arranca tras cambiar DATABASE_URL
→ Revisar logs en Render (Dashboard → Web Service → Logs). Error típico: URL mal formateada
