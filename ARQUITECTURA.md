# 🏗️ ARQUITECTURA DEL PROYECTO PORTFOLIO

**Última actualización:** 13 Enero 2026

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

### Página Admin (`/admin`) - Futuro:
- Login con JWT
- CRUD de proyectos destacados
- CRUD de cursos/certificaciones
- Gestión de contenido
- Visualización de analíticas

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
    video_url: str (opcional)
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
    titulo: str
    institucion: str
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
    orden: int
    activo: bool
    mostrar_en_web: bool (solo mostrar 1-2 más recientes)
```

### 4. Tabla `github_repos_cache` (Cache de GitHub)
```python
class GitHubRepoCache(Base):
    id: int (PK)
    repo_name: str
    descripcion: str
    url: str
    lenguaje: str
    estrellas: int
    forks: int
    fecha_actualizacion: datetime
    ultimo_fetch: datetime
```

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

### 6. Tabla `users` (Admin)
```python
class User(Base):
    id: int (PK)
    username: str (unique)
    email: str (unique)
    hashed_password: str
    is_admin: bool
    fecha_creacion: datetime
    ultimo_login: datetime
```

---

## 🔌 Endpoints de la API

### Endpoints Públicos (sin autenticación):

```
GET  /api/proyectos              → Listar proyectos destacados activos
GET  /api/proyectos/{id}         → Obtener proyecto por ID
GET  /api/cursos                 → Listar cursos/certificaciones activos
GET  /api/cursos/{id}            → Obtener curso por ID
GET  /api/experiencias           → Listar experiencias actuales/recientes
GET  /api/experiencias/{id}      → Obtener experiencia por ID
GET  /api/github/repos           → Listar repos de GitHub (con cache)
POST /api/contacto               → Enviar mensaje de contacto
POST /api/analytics              → Registrar evento de analítica
```

### Endpoints Protegidos (requieren JWT):

```
POST   /api/auth/login           → Login admin
POST   /api/auth/refresh         → Refresh token
GET    /api/admin/analytics      → Obtener estadísticas
POST   /api/admin/proyectos      → Crear proyecto
PUT    /api/admin/proyectos/{id} → Actualizar proyecto
DELETE /api/admin/proyectos/{id} → Eliminar proyecto
POST   /api/admin/cursos         → Crear curso
PUT    /api/admin/cursos/{id}    → Actualizar curso
DELETE /api/admin/cursos/{id}    → Eliminar curso
POST   /api/admin/experiencias    → Crear experiencia
PUT    /api/admin/experiencias/{id} → Actualizar experiencia
DELETE /api/admin/experiencias/{id} → Eliminar experiencia
```

---

## 🚀 Plan de Despliegue

### Desarrollo:
```
Frontend: localhost:3000 (Reflex dev server)
Backend:  localhost:8000 (Uvicorn)
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

### 4. Panel Admin (Futuro):
```
Admin hace login
         ↓
    POST /api/auth/login
         ↓
    Backend valida credenciales
         ↓
    Retorna JWT token
         ↓
    Frontend guarda token
         ↓
    Admin crea/edita contenido
         ↓
    Requests con Authorization: Bearer {token}
         ↓
    Backend valida JWT y procesa
         ↓
    DB actualizada
         ↓
    Frontend público muestra cambios
```

---

## 🔒 Seguridad

### Medidas Implementadas:
- ✅ Validación de formularios en frontend
- ✅ CORS configurado correctamente
- 🔄 Sanitización de inputs en backend (pendiente)
- 🔄 Rate limiting en endpoints (pendiente)
- 🔄 JWT para autenticación admin (pendiente)
- 🔄 Hashing de contraseñas con bcrypt (pendiente)
- 🔄 HTTPS en producción (automático con Vercel/Fly.io)
- 🔄 Variables de entorno para secrets (pendiente)
- 🔄 IP anónima en analytics (solo 3 primeros octetos)

---

## 📈 Próximos Pasos (Prioridad)

### Fase 4 - Backend (Próxima sesión):
1. Setup FastAPI inicial
2. Configurar SQLAlchemy + SQLite
3. Crear modelos (Proyecto, Curso, Certificacion)
4. Endpoints CRUD básicos
5. Integración GitHub API con cache
6. Conectar frontend con backend

### Fase 5 - Integración:
1. Fetch datos desde API en frontend
2. Loading states
3. Error handling
4. Dinamizar sección Proyectos
5. Crear sección Formación
6. Crear sección GitHub Repos

### Fase 6 - Admin Panel:
1. Sistema de autenticación JWT
2. Página login
3. Dashboard admin
4. CRUD proyectos
5. CRUD cursos

### Fase 7 - Analíticas:
1. Middleware para tracking
2. Geolocalización de IPs
3. Dashboard de visualización
4. Exportación de datos

### Fase 8-10:
- SEO y optimización
- Testing
- Despliegue en producción

---

**Documento vivo - Se actualizará conforme avance el proyecto**
