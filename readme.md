# Portfolio - Alessandro Febbrai

Portfolio personal full-stack desarrollado con **Reflex** (frontend) y **FastAPI** (backend).

---

## Características

- **Multi-idioma** — ES / EN / IT / CA con traducciones completas (100+ textos)
- **Diseño minimalista** — Interfaz B/N, glassmorphism navbar, animaciones CSS, cards con hover
- **Typing animation** — Roles rotativos en hero (JS typing effect), cambia idioma instantáneamente desde `translations.py`
- **Panel admin protegido** — CRUD completo para proyectos, cursos/formación y experiencias
- **Media uploads (Cloudinary)** — Imágenes, PDFs y videos subidos a Cloudinary
- **Analíticas** — Tracking de visitas con dashboard CSS puro (sin recharts): stat cards, barras visuales, badges, export Excel
- **Formulario de contacto** — Envío de emails via Resend API
- **Autenticación JWT** — Login seguro con cambio de contraseña y username
- **GitHub API** — Repositorios cargados automáticamente con cache 6h
- **Responsive** — Adaptado a móvil, tablet y desktop con CSS media queries
- **SEO** — Metatags, OpenGraph, Twitter Cards, robots.txt
- **Visor CV/Diploma** — PDFs inline visualizables y descargables
- **Soft delete** — Los registros se desactivan (`activo=False`) en lugar de borrarse
- **Colores por tipo** — Formación: diploma=amarillo, curso=cyan, certificación=naranja · Experiencia: práctica=cyan, trabajo=verde · Proyectos: púrpura

---

## Uploads (Cloudinary)

| Tipo | Flujo | Límite |
|------|-------|--------|
| **Imagen** | Browser → Reflex Cloud → Render backend → Cloudinary | 10 MB |
| **PDF** | Browser → Reflex Cloud → Render backend → Cloudinary | 10 MB |
| **Video** | Browser → **Cloudinary directo** (1 salto, sin pasar por Render) | 100 MB |

Los videos se suben directamente desde el navegador a Cloudinary usando una firma generada por el backend (`GET /api/upload/sign`). Esto evita los timeouts y límites de tamaño de Reflex Cloud y Render.

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| **Frontend** | Reflex 0.8+ (Python → React/Vite), CSS custom |
| **Backend** | FastAPI, SQLAlchemy, PostgreSQL (Neon serverless) |
| **Auth** | JWT (python-jose), bcrypt |
| **Email** | Resend API |
| **Media** | Cloudinary (image, raw, video) |
| **Analytics** | `rx.call_script` + callback websocket + FastAPI endpoint |
| **Monitoring** | UptimeRobot (ping `/health` cada 5 min) |
| **Hosting** | Reflex Cloud (frontend) + Render (backend) + Neon (PostgreSQL) |
| **Control de versiones** | Git + GitHub |

---

## Despliegue en Producción

| Servicio | Plataforma | URL |
|----------|-----------|-----|
| **Frontend** | Reflex Cloud | `https://portfolio-alessandro-teal-moon.reflex.run` |
| **Backend** | Render (free tier) | `https://portfolio-reflex-pwdv.onrender.com` |
| **Base de datos** | Neon PostgreSQL (serverless) | Conectada via `DATABASE_URL` con SSL |

### Flujo de trabajo

| Cambio | Acción |
|--------|--------|
| **Backend** | `git push origin main` → Render redeploy automático |
| **Frontend** | `git push origin main` + ejecutar `reflex deploy --app-name portfolio-alessandro` desde `frontend/` |

> **Nota:** El free tier de Render entra en sleep tras 15 min de inactividad. Se usa UptimeRobot (ping cada 5 min a `/health`) para mantenerlo activo.

---

## Estructura del Proyecto

```
mi_portfolio_reflex/
├── frontend/
│   ├── mi_portfolio_reflex/
│   │   ├── mi_portfolio_reflex.py    # App principal, rutas, SEO metatags
│   │   ├── translations.py           # Traducciones (ES, EN, IT, CA)
│   │   ├── models.py                 # Modelos Pydantic (Proyecto, Curso, Experiencia, GitHubRepo)
│   │   ├── utils.py                  # Funciones auxiliares
│   │   ├── state.py                  # Re-export de states/
│   │   ├── states/
│   │   │   └── __init__.py           # State unificado (auth, CRUD, uploads, analytics, contacto)
│   │   ├── components/
│   │   │   ├── navbar.py             # Navbar glassmorphism con menú hamburguesa
│   │   │   ├── footer.py             # Footer con links sociales
│   │   │   ├── selectors.py          # Selector de idioma
│   │   │   └── skeletons.py          # Loading skeletons
│   │   ├── sections/
│   │   │   ├── sobre_mi.py           # Sección "Sobre mí" + tech stack
│   │   │   ├── experiencia.py        # Experiencias laborales/prácticas
│   │   │   ├── formacion.py          # Cursos, diplomas, certificaciones
│   │   │   ├── proyectos.py          # Proyectos con video/imagen
│   │   │   ├── github.py             # Repositorios GitHub
│   │   │   └── contacto.py           # Formulario de contacto
│   │   ├── pages/
│   │   │   ├── portada.py            # Landing con foto, nombre, selector idioma
│   │   │   ├── home.py               # Página principal (todas las secciones)
│   │   │   ├── cv.py                 # Visor PDF del CV
│   │   │   ├── diploma.py            # Visor PDF de diplomas/certificados
│   │   │   └── login.py              # Login admin
│   │   └── admin/
│   │       ├── dashboard.py          # Dashboard admin principal
│   │       ├── proyectos.py          # CRUD proyectos (imagen + video upload)
│   │       ├── cursos.py             # CRUD cursos/formación (certificado + diploma upload)
│   │       ├── experiencias.py       # CRUD experiencias (imagen + video + documento upload)
│   │       └── analytics.py          # Dashboard analíticas + export Excel
│   ├── assets/
│   │   ├── CV.pdf                    # Currículum
│   │   ├── foto_perfil.png           # Foto de perfil
│   │   ├── favicon.ico               # Favicon
│   │   ├── robots.txt                # SEO
│   │   └── styles/
│   │       └── styles.css            # CSS: animaciones, responsive, glassmorphism
│   └── rxconfig.py                   # Configuración Reflex (puerto 3000)
│
├── backend/
│   ├── app/
│   │   ├── main.py                   # FastAPI app, CORS, migraciones auto, crear admin
│   │   ├── config.py                 # Settings (pydantic-settings, lee .env)
│   │   ├── database.py               # SQLAlchemy engine (Neon SSL + pool_pre_ping)
│   │   ├── models/
│   │   │   ├── proyecto.py           # Modelo Proyecto (multi-idioma, imagen, video)
│   │   │   ├── curso.py              # Modelo Curso (tipo, certificado, diploma)
│   │   │   ├── experiencia.py        # Modelo Experiencia (imagen, video, documento)
│   │   │   ├── user.py               # Modelo User (admin)
│   │   │   ├── visita.py             # Modelo Visita (analytics)
│   │   │   └── github_repo.py        # Modelo GitHubRepo (cache)
│   │   ├── schemas/
│   │   │   ├── proyecto.py           # Pydantic: ProyectoCreate, ProyectoUpdate, Proyecto
│   │   │   ├── curso.py              # Pydantic: CursoCreate, CursoUpdate, Curso
│   │   │   ├── experiencia.py        # Pydantic: ExperienciaCreate, ExperienciaUpdate
│   │   │   ├── auth.py               # Pydantic: Token, UserCreate, ChangePassword/Username
│   │   │   └── github_repo.py        # Pydantic: GitHubRepoResponse
│   │   ├── routers/
│   │   │   ├── proyectos.py          # CRUD /api/proyectos/
│   │   │   ├── cursos.py             # CRUD /api/cursos/
│   │   │   ├── experiencias.py       # CRUD /api/experiencias/
│   │   │   ├── auth.py               # Login, register, change-password/username
│   │   │   ├── upload.py             # Upload a Cloudinary + firma para upload directo
│   │   │   ├── contacto.py           # Envío emails (Resend)
│   │   │   ├── github.py             # GitHub API + cache 6h
│   │   │   └── analytics.py          # Tracking público + consultas admin + export Excel
│   │   ├── middleware/
│   │   │   └── analytics.py          # Middleware analytics (legacy)
│   │   └── utils/
│   │       └── auth.py               # JWT encode/decode, password hashing (bcrypt)
│   ├── scripts/
│   │   ├── migrate_render_to_neon.py # Migración DB via SQLAlchemy (env vars)
│   │   ├── verify_db.py              # Verificación tablas y datos
│   │   └── MIGRATION_NEON.md         # Guía de migración
│   ├── create_admin.py               # Script manual para crear admin
│   ├── render.yaml                   # Config despliegue Render
│   └── requirements.txt              # Dependencias backend
│
├── .env                              # Variables de entorno (NO en Git)
├── .gitignore
└── readme.md                         # Este archivo
```

---

## Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Portada — foto con glow animado, nombre, rol, selector de idioma, animaciones escalonadas |
| `/home` | Página principal — Sobre mí, Experiencia, Formación, Proyectos, GitHub, Contacto |
| `/cv` | Visor PDF del CV a pantalla completa |
| `/diploma` | Visor PDF de diplomas y certificados |
| `/login` | Login admin |
| `/admin` | Dashboard admin |
| `/admin/proyectos` | Lista + CRUD proyectos |
| `/admin/proyectos/form` | Formulario crear/editar proyecto |
| `/admin/cursos` | Lista + CRUD cursos/formación |
| `/admin/cursos/form` | Formulario crear/editar curso |
| `/admin/experiencias` | Lista + CRUD experiencias |
| `/admin/experiencias/form` | Formulario crear/editar experiencia |
| `/admin/analytics` | Dashboard analíticas (CSS bars + badges) y export Excel |

---

## API Endpoints

### Contenido (CRUD)

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| GET | `/api/proyectos/` | — | Listar proyectos (`?destacados=true`, `?limit=N`) |
| GET | `/api/proyectos/{id}` | — | Obtener proyecto por ID |
| POST | `/api/proyectos/` | JWT | Crear proyecto |
| PUT | `/api/proyectos/{id}` | JWT | Actualizar proyecto |
| DELETE | `/api/proyectos/{id}` | JWT | Soft delete proyecto |
| GET | `/api/cursos/` | — | Listar cursos activos |
| GET | `/api/cursos/{id}` | — | Obtener curso por ID |
| POST | `/api/cursos/` | JWT | Crear curso |
| PUT | `/api/cursos/{id}` | JWT | Actualizar curso |
| DELETE | `/api/cursos/{id}` | JWT | Soft delete curso |
| GET | `/api/experiencias/` | — | Listar experiencias activas |
| GET | `/api/experiencias/{id}` | — | Obtener experiencia por ID |
| POST | `/api/experiencias/` | JWT | Crear experiencia |
| PUT | `/api/experiencias/{id}` | JWT | Actualizar experiencia |
| DELETE | `/api/experiencias/{id}` | JWT | Soft delete experiencia |

### Autenticación

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/auth/login` | — | Login (OAuth2, retorna JWT) |
| POST | `/api/auth/register` | — | Registrar usuario |
| GET | `/api/auth/me` | JWT | Info usuario actual |
| PUT | `/api/auth/change-password` | JWT | Cambiar contraseña (mín. 6 chars) |
| PUT | `/api/auth/change-username` | JWT | Cambiar username (mín. 3 chars, único) |

### Uploads (Cloudinary)

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/upload/` | JWT | Subir imagen/PDF/video vía backend (chunked para video) |
| GET | `/api/upload/sign` | JWT | Obtener firma Cloudinary para upload directo desde browser |

### Otros

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| GET | `/api/github/repos` | — | Repos GitHub (cache 6h, `?force_refresh=true`) |
| DELETE | `/api/github/cache` | — | Limpiar cache repos |
| POST | `/api/contacto/` | — | Enviar email de contacto (Resend) |
| GET | `/` | — | Root: status de la API |
| GET | `/health` | — | Health check |

### Analíticas

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/analytics/track` | — | Registrar visita (público, llamado desde JS) |
| GET | `/api/analytics/resumen` | JWT | Total visitas + únicos (últimos N días) |
| GET | `/api/analytics/paginas` | JWT | Páginas más visitadas |
| GET | `/api/analytics/dispositivos` | JWT | Distribución dispositivos |
| GET | `/api/analytics/navegadores` | JWT | Distribución navegadores |
| GET | `/api/analytics/plataformas` | JWT | Distribución SO |
| GET | `/api/analytics/referrers` | JWT | Origen del tráfico |
| GET | `/api/analytics/visitas-por-dia` | JWT | Visitas agrupadas por día |
| GET | `/api/analytics/recientes` | JWT | Últimas visitas detalladas |
| GET | `/api/analytics/export` | JWT | Export a Excel (.xlsx) |

---

## Sistema de Analíticas

El tracking funciona con **`rx.call_script`** ejecutado en el navegador del visitante:

1. `on_load=State.registrar_visita` en cada página pública dispara `rx.call_script`
2. El JS recoge: user agent, resolución pantalla, idioma, plataforma, referrer, página
3. El callback `State.enviar_tracking` recibe el JSON via websocket y envía al backend con `httpx.post`
4. El backend (`POST /api/analytics/track`) detecta dispositivo, navegador y SO, y almacena la visita en PostgreSQL
5. El dashboard admin muestra métricas con CSS bars, badges y stat cards + export a Excel

> **Nota técnica:** En Reflex 0.8 (Vite), `rx.script`, `head_components` y `rx.el.script` **no funcionan** en producción (Reflex Cloud). La única forma fiable es `rx.call_script` con callback.

---

## Diseño Visual

- **Portada**: Foto circular con glow pulse animado, animaciones escalonadas (fade-in)
- **Navbar**: Glassmorphism (`backdrop-filter: blur`), links con underline animado, menú hamburguesa móvil
- **Hero**: Foto 180px con borde gradiente
- **Cards**: Bordes `rgba` sutiles, hover con iluminación + elevación
- **Formación**: Colores por tipo — diploma (amarillo), curso (cyan), certificación (naranja)
- **Experiencia**: Colores por tipo — práctica (cyan), trabajo (verde)
- **Proyectos**: Títulos en púrpura, video HTML5 + imagen Cloudinary
- **Paleta**: Negro `#000`, blanco, grises `rgba(255,255,255,0.xx)`

---

## Instalación local

```bash
# Clonar
git clone https://github.com/geobest7/portfolio_reflex.git
cd mi_portfolio_reflex

# Entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
pip install -r requirements.txt
reflex init
```

### Variables de entorno

Crear archivo `.env` en la **raíz** del proyecto:

```env
# Base de datos
DATABASE_URL=postgresql://user:pass@host/dbname  # Neon o PostgreSQL local

# Seguridad
SECRET_KEY=tu-clave-secreta-muy-larga

# GitHub
GITHUB_TOKEN=tu-token-github

# CORS
CORS_ALLOW_ALL=false

# Contacto (Resend)
RESEND_API_KEY=tu-api-key-resend
CONTACT_EMAIL_TO=tu-email-destino

# Cloudinary
CLOUDINARY_CLOUD_NAME=tu-cloud-name
CLOUDINARY_API_KEY=tu-api-key
CLOUDINARY_API_SECRET=tu-api-secret
```

### Ejecutar en local

```bash
# Terminal 1 — Backend
cd backend
uvicorn app.main:app --reload --port 8001

# Terminal 2 — Frontend
cd frontend
reflex run
```

- **Frontend**: `http://localhost:3000`
- **Backend API + Swagger**: `http://localhost:8001/docs`

### Desplegar a producción

```bash
# 1. Push (Render redeploy automático del backend)
git add .
git commit -m "descripción del cambio"
git push origin main

# 2. Deploy frontend (solo si hay cambios en frontend/)
cd frontend
reflex deploy --app-name portfolio-alessandro
```

---

## Autor

**Alessandro Febbrai**
- Email: febbrai.alessandro@libero.it
- LinkedIn: [alessandro-febbrai](https://www.linkedin.com/in/alessandro-febbrai-b239021a2)
- GitHub: [geobest7](https://github.com/geobest7)

---

## Licencia

Todos los derechos reservados.
