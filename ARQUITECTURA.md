# 🏗️ ARQUITECTURA DEL PROYECTO PORTFOLIO

**Última actualización:** 4 Febrero 2026 (mejoras de diseño, UI admin)

---

## 📐 Visión General

Portfolio personal full-stack con contenido dinámico, multi-idioma, y panel de administración.

### Objetivos del Proyecto:
1. **Escalabilidad:** Poder añadir/editar contenido sin modificar código
2. **Profesionalidad:** Mostrar proyectos destacados y formación técnica
3. **Mantenibilidad:** Arquitectura clara y bien documentada
4. **Multi-idioma:** Soporte completo para 4 idiomas (ES, EN, IT, CA)
5. **Responsive:** Funcional en móvil, tablet y desktop

---

## 🎯 Estructura de Secciones del Portfolio

### Página Principal (`/home`):

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR (sticky)                                    │
│  Logo | Inicio | Sobre mí | Proyectos | GitHub |   │
│  Formación | Contacto | CV | [Selector idioma]     │
├─────────────────────────────────────────────────────┤
│  1. HERO SECTION                                    │
│     - Nombre: Alessandro Febbrai                    │
│     - Rol: Desarrollador Python                     │
│     - Descripción breve                             │
├─────────────────────────────────────────────────────┤
│  2. SOBRE MÍ (expandida)                            │
│     - Descripción personal                          │
│     - Badges de habilidades técnicas                │
│     - EXPERIENCIA ACTUAL (subsección)               │
│       • Prácticas en desarrollo                     │
│       • Empresa, rol, período                       │
│       • Tecnologías utilizadas                      │
│       • Descripción breve de tareas                 │
│       • Solo mostrar experiencia actual o reciente  │
├─────────────────────────────────────────────────────┤
│  3. PROYECTOS DESTACADOS (desde DB)                 │
│     - 3-5 proyectos curados                         │
│     - Descripción detallada                         │
│     - Tecnologías usadas                            │
│     - Links: GitHub, Demo live                      │
│     - Capturas/videos                               │
├─────────────────────────────────────────────────────┤
│  4. REPOSITORIOS GITHUB (desde GitHub API)          │
│     - Listado completo de repos públicos            │
│     - Actualización automática                      │
│     - Filtrado por lenguaje/estrellas               │
│     - Muestra actividad y contribuciones            │
├─────────────────────────────────────────────────────┤
│  5. FORMACIÓN (desde DB)                            │
│     - Diploma oficial (título italiano)             │
│     - Cursos completados (Platzi, Udemy, etc.)      │
│     - Certificaciones oficiales                     │
│     - Tecnologías aprendidas                        │
├─────────────────────────────────────────────────────┤
│  6. CONTACTO                                        │
│     - Información de contacto (email, tel, etc.)    │
│     - Formulario funcional con validación           │
│     - Mensajes de éxito/error multi-idioma          │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
│  Links sociales | Copyright                         │
└─────────────────────────────────────────────────────┘
```

**Nota sobre Experiencia:**
- Se incluye como subsección dentro de "Sobre mí" para mantener navbar limpia (6 links)
- Solo se muestran experiencias actuales o las 2 más recientes
- Escalable: si en el futuro hay 3+ experiencias, se puede migrar a sección independiente
- El CV en PDF contiene el historial laboral completo

### Página CV (`/cv`):
- Visor PDF a pantalla completa
- Contiene experiencia laboral completa
- No duplicar contenido en la web

### Página Admin (`/admin`) - ✅ IMPLEMENTADO:
- Login con JWT (/login)
- Dashboard protegido (/admin)
- CRUD de proyectos destacados (/admin/proyectos)
- CRUD de cursos/certificaciones (/admin/cursos)
- CRUD de experiencias (/admin/experiencias)
- Formularios multi-idioma para crear/editar
- Protección de rutas con autenticación

---

## 🏛️ Arquitectura Técnica

### Stack Tecnológico:

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND                         │
│  Reflex (Python) → React (generado automáticamente) │
│  - Multi-idioma con estado global                   │
│  - Responsive design (CSS + Media queries)          │
│  - Formularios con validación                       │
│  - Consumo de API REST                              │
└─────────────────────────────────────────────────────┘
                         ↕ HTTP/REST
┌─────────────────────────────────────────────────────┐
│                    BACKEND                          │
│  FastAPI (Python)                                   │
│  - Endpoints CRUD para contenido                    │
│  - Autenticación JWT (admin)                        │
│  - Integración GitHub API                           │
│  - Sistema de analíticas                            │
└─────────────────────────────────────────────────────┘
                         ↕ SQLAlchemy ORM
┌─────────────────────────────────────────────────────┐
│                  BASE DE DATOS                      │
│  SQLite (desarrollo) / PostgreSQL (producción)      │
│  - Tabla: proyectos                                 │
│  - Tabla: cursos                                    │
│  - Tabla: experiencias                              │
│  - Tabla: github_repos_cache                        │
│  - Tabla: analytics                                 │
│  - Tabla: users (admin)                             │
└─────────────────────────────────────────────────────┘
```

---

## 🗄️ Modelos de Base de Datos

### 1. Tabla `proyectos` (Proyectos Destacados)
```python
class Proyecto(Base):
    id: int (PK)
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    descripcion_es: text
    descripcion_en: text
    descripcion_it: text
    descripcion_ca: text
    tecnologias: str (JSON: ["Python", "FastAPI", ...])
    url_github: str
    url_demo: str (opcional)
    imagen_url: str
    video_url: str (opcional, URL YouTube embed)
    orden: int (para ordenar en frontend)
    destacado: bool
    fecha_creacion: datetime
    activo: bool
```

### 2. Tabla `cursos` (Cursos y Certificaciones)
```python
class Curso(Base):
    id: int (PK)
    tipo: str ("diploma", "curso", "certificacion")
    titulo_es: str
    titulo_en: str
    titulo_it: str
    titulo_ca: str
    institucion_es: str
    institucion_en: str
    institucion_it: str
    institucion_ca: str
    fecha_inicio: date
    fecha_fin: date (opcional, si aún está en curso)
    descripcion_es: text
    descripcion_en: text
    descripcion_it: text
    descripcion_ca: text
    tecnologias: str (JSON: ["Python", "FastAPI", ...])
    certificado_url: str (opcional, link al certificado)
    imagen_url: str (opcional, logo de la institución)
    orden: int
    activo: bool
```

### 3. Tabla `experiencias` (Experiencia Laboral)
```python
class Experiencia(Base):
    id: int (PK)
    tipo: str ("practica", "trabajo", "freelance")
    empresa: str
    cargo_es: str
    cargo_en: str
    cargo_it: str
    cargo_ca: str
    fecha_inicio: date
    fecha_fin: date (opcional, si es actual)
    actual: bool (si es la experiencia actual)
    descripcion_es: text
    descripcion_en: text
    descripcion_it: text
    descripcion_ca: text
    tecnologias: str (JSON: ["Python", "FastAPI", ...])
    video_url: str (opcional, URL YouTube embed)
    orden: int
    activo: bool
    mostrar_en_web: bool (solo mostrar 1-2 más recientes)
```

### 4. Tabla `github_repos` (Cache de GitHub) - ✅ IMPLEMENTADO
```python
class GitHubRepo(Base):
    id: int (PK)
    repo_id: int (unique, ID de GitHub)
    name: str
    description: str
    html_url: str
    language: str
    stargazers_count: int
    forks_count: int
    topics: str (JSON: ["python", "fastapi", ...])
    cached_at: datetime
    activo: bool
```
**Cache TTL:** 6 horas (21600 segundos)

### 5. Tabla `analytics` (Sistema de Analíticas)
```python
class Analytics(Base):
    id: int (PK)
    fecha: datetime
    ip_anonima: str (solo primeros 3 octetos)
    pais: str
    ciudad: str
    dispositivo: str ("mobile", "tablet", "desktop")
    navegador: str
    pagina_visitada: str
    accion: str ("visita", "click_proyecto", "descarga_cv", "envio_formulario")
    referrer: str (opcional)
```

### 6. Tabla `users` (Admin) - ✅ IMPLEMENTADO
```python
class User(Base):
    id: int (PK)
    username: str (unique)
    email: str (unique)
    hashed_password: str (bcrypt)
    is_active: bool
    is_admin: bool
```
**Seguridad:**
- Contraseñas hasheadas con bcrypt 4.0.1
- JWT tokens con expiración de 30 minutos
- SECRET_KEY en .env

---

## 🔌 Endpoints de la API

### Endpoints Públicos (sin autenticación):

```
GET  /api/proyectos              → Listar proyectos (filtro: destacados)
GET  /api/proyectos/{id}         → Obtener proyecto por ID
GET  /api/cursos                 → Listar cursos activos
GET  /api/cursos/{id}            → Obtener curso por ID
GET  /api/experiencias           → Listar experiencias (filtro: mostrar_en_web)
GET  /api/experiencias/{id}      → Obtener experiencia por ID
GET  /api/github/repos           → Listar repos de GitHub (con cache 6h) ✅
POST /api/contacto               → Enviar mensaje de contacto (pendiente)
POST /api/analytics              → Registrar evento de analítica (pendiente)
```

### Endpoints Protegidos (requieren JWT):

**Autenticación:** ✅ IMPLEMENTADO
```
POST   /api/auth/login           → Login admin (OAuth2)
GET    /api/auth/me              → Obtener usuario actual
POST   /api/auth/register        → Registrar usuario (solo admin)
```

**CRUD Proyectos:** ✅ IMPLEMENTADO
```
POST   /api/proyectos            → Crear proyecto (solo admin)
PUT    /api/proyectos/{id}       → Actualizar proyecto (solo admin)
DELETE /api/proyectos/{id}       → Eliminar proyecto - soft delete (solo admin)
```

**CRUD Cursos:** ✅ IMPLEMENTADO
```
POST   /api/cursos               → Crear curso (solo admin)
PUT    /api/cursos/{id}          → Actualizar curso (solo admin)
DELETE /api/cursos/{id}          → Eliminar curso - soft delete (solo admin)
```

**CRUD Experiencias:** ✅ IMPLEMENTADO
```
POST   /api/experiencias         → Crear experiencia (solo admin)
PUT    /api/experiencias/{id}    → Actualizar experiencia (solo admin)
DELETE /api/experiencias/{id}    → Eliminar experiencia - soft delete (solo admin)
```

**GitHub API:** ✅ IMPLEMENTADO
```
DELETE /api/github/cache          → Limpiar cache de repositorios (solo admin)
```

**Analíticas:** (pendiente)
```
GET    /api/admin/analytics      → Obtener estadísticas
```

---

## 🚀 Plan de Despliegue

### Desarrollo:
```
Frontend: localhost:3000 (Reflex dev server)
Backend:  localhost:8001 (Uvicorn)
DB:       SQLite local (portfolio.db)
```

### Producción:

```
┌─────────────────────────────────────────────────────┐
│  VERCEL (Frontend)                                  │
│  - Deploy automático desde GitHub                   │
│  - CDN global                                       │
│  - HTTPS automático                                 │
│  - Variables de entorno: API_URL                    │
└─────────────────────────────────────────────────────┘
                         ↕ HTTPS/REST
┌─────────────────────────────────────────────────────┐
│  FLY.IO / RENDER (Backend)                          │
│  - Deploy desde GitHub                              │
│  - Escalado automático                              │
│  - HTTPS automático                                 │
│  - Variables de entorno: DATABASE_URL, SECRET_KEY   │
└─────────────────────────────────────────────────────┘
                         ↕ PostgreSQL
┌─────────────────────────────────────────────────────┐
│  POSTGRESQL (Base de Datos)                         │
│  - Fly.io Postgres / Render PostgreSQL              │
│  - Backups automáticos                              │
│  - Conexión segura (SSL)                            │
└─────────────────────────────────────────────────────┘
```

---

## 📊 Flujo de Datos

### 1. Carga Inicial de Página:
```
Usuario → Frontend (Reflex)
         ↓
    Fetch datos desde API
         ↓
    Backend (FastAPI) → DB (SQLAlchemy)
         ↓
    Retorna JSON
         ↓
    Frontend renderiza contenido dinámico
```

### 2. Cambio de Idioma:
```
Usuario selecciona idioma
         ↓
    Estado global actualizado (state.py)
         ↓
    Todas las traducciones reactivas se actualizan
         ↓
    Contenido de DB se muestra en idioma seleccionado
```

### 3. Envío de Formulario:
```
Usuario llena formulario
         ↓
    Validación en frontend (state.py)
         ↓
    POST /api/contacto (si válido)
         ↓
    Backend procesa y envía email
         ↓
    Registra en analytics
         ↓
    Retorna éxito/error
         ↓
    Frontend muestra mensaje traducido
```

### 4. Panel Admin: ✅ IMPLEMENTADO
```
Admin hace login en /login
         ↓
    POST /api/auth/login (OAuth2)
         ↓
    Backend valida credenciales (bcrypt)
         ↓
    Retorna JWT token (exp: 30min)
         ↓
    Frontend guarda token en State
         ↓
    Admin accede a /admin (dashboard)
         ↓
    Admin navega a /admin/proyectos|cursos|experiencias
         ↓
    Admin crea/edita contenido en formularios multi-idioma
         ↓
    Requests con Authorization: Bearer {token}
         ↓
    Backend valida JWT con get_current_admin_user
         ↓
    DB actualizada (soft delete para eliminaciones)
         ↓
    Frontend público muestra cambios inmediatamente
```

---

## 🔒 Seguridad

### Medidas Implementadas:
- ✅ Validación de formularios en frontend
- ✅ CORS configurado correctamente
- ✅ JWT para autenticación admin (python-jose)
- ✅ Hashing de contraseñas con bcrypt 4.0.1
- ✅ Variables de entorno para secrets (.env con SECRET_KEY, GITHUB_TOKEN)
- ✅ Protección de endpoints CRUD (solo admin puede modificar)
- ✅ Soft delete en lugar de borrado físico
- 🔄 Sanitización de inputs en backend (pendiente)
- 🔄 Rate limiting en endpoints (pendiente)
- 🔄 HTTPS en producción (automático con Vercel/Fly.io)
- 🔄 IP anónima en analytics (solo 3 primeros octetos)

---

## 📈 Estado Actual y Próximos Pasos

### ✅ COMPLETADO:

**Fase 1-3:** Setup, Multi-idioma, Frontend básico
**Fase 4:** Backend FastAPI con SQLAlchemy + SQLite
**Fase 5:** Integración Frontend-Backend completa
**Fase 6:** Optimizaciones (skeleton loaders, animaciones, auto-carga)
**Fase 7:** GitHub API con cache de 6 horas
**Fase 8:** Autenticación JWT completa
**Fase 9:** Panel Admin CRUD completo (Proyectos, Cursos, Experiencias)
**Fase 10:** Videos YouTube embebidos en Proyectos y Experiencias

### 🔄 EN PROGRESO:

**Fase 10 - Funcionalidades Adicionales:**
1. Formulario de contacto funcional (backend)
2. Envío de emails desde formulario
3. Validación avanzada de inputs

### ⏳ PENDIENTE:

**Fase 11 - Sistema de Analíticas:**
1. Middleware para tracking de visitas
2. Geolocalización de IPs (anónimas)
3. Tracking de clicks en proyectos
4. Dashboard de visualización en /admin
5. Exportación de datos (CSV/Excel)

**Fase 12 - SEO y Optimización:**
1. Metatags dinámicos
2. OpenGraph y Twitter Cards
3. Sitemap.xml
4. Robots.txt
5. Performance optimization

**Fase 13 - Testing y Despliegue:**
1. Testing end-to-end
2. Deploy frontend en Vercel
3. Deploy backend en Fly.io/Render
4. PostgreSQL en producción
5. Dominio personalizado

---

**Documento vivo - Se actualizará conforme avance el proyecto**
