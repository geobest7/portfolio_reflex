# Portfolio - Alessandro Febbrai

Portfolio personal full-stack desarrollado con **Reflex** (frontend) y **FastAPI** (backend).

---

## Características

- **Multi-idioma** — ES / EN / IT / CA con traducciones completas
- **Diseño minimalista** — Interfaz B/N, glassmorphism, animaciones CSS, cards con hover
- **Panel admin** — CRUD completo para proyectos, cursos y experiencias
- **Analíticas reales** — Tracking via `rx.call_script` + callback, dashboard con dispositivos, SO, navegadores, referrers y export Excel
- **Formulario de contacto** — Envío de emails via Resend API
- **Autenticación JWT** — Login seguro para admin con cambio de credenciales
- **GitHub API** — Repositorios cargados automáticamente con cache 6h
- **Responsive** — Adaptado a móvil, tablet y desktop
- **SEO** — Metatags, OpenGraph, Twitter Cards, robots.txt
- **Visor CV/Diploma** — PDFs visualizables y descargables

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| **Frontend** | Reflex (Python → React), CSS custom |
| **Backend** | FastAPI, SQLAlchemy, PostgreSQL (prod) / SQLite (local) |
| **Auth** | JWT (python-jose), bcrypt |
| **Email** | Resend API |
| **Analytics** | `rx.call_script` callback + endpoint público + dashboard admin |
| **Hosting** | Reflex Cloud (frontend) + Render (backend + PostgreSQL) |
| **Control de versiones** | Git + GitHub |

---

## Despliegue en Producción

| Servicio | Plataforma | URL |
|----------|-----------|-----|
| **Frontend** | Reflex Cloud | `https://portfolio-alessandro-teal-moon.reflex.run` |
| **Backend** | Render | `https://portfolio-reflex-pwdv.onrender.com` |
| **Base de datos** | Render PostgreSQL | Interna (no accesible desde fuera) |

### Flujo de trabajo

| Cambio | Acción |
|--------|--------|
| **Backend** | `git push origin main` → Render redeploy automático |
| **Frontend** | `git push origin main` + ejecutar `reflex deploy --app-name portfolio-alessandro` desde `frontend/` |

---

## Estructura del Proyecto

```
mi_portfolio_reflex/
├── frontend/
│   ├── mi_portfolio_reflex/
│   │   ├── mi_portfolio_reflex.py    # App principal + rutas + SEO
│   │   ├── translations.py           # Traducciones (ES, EN, IT, CA)
│   │   ├── models.py                 # Modelos Pydantic
│   │   ├── utils.py                  # Helpers
│   │   ├── states/                   # State unificado (auth, analytics, CRUD, contacto)
│   │   ├── components/               # Navbar, footer, selectores, skeletons
│   │   ├── sections/                 # Sobre mí, proyectos, formación, experiencia, github, contacto
│   │   ├── pages/                    # Portada, home, CV, login
│   │   └── admin/                    # Dashboard, CRUD proyectos/cursos/experiencias, analíticas
│   ├── assets/                       # CV.pdf, foto_perfil.png, favicon.ico, tracking.js, styles/
│   └── rxconfig.py
│
├── backend/
│   ├── app/
│   │   ├── main.py                   # FastAPI + CORS + migración DB + auto-crear admin
│   │   ├── config.py                 # Settings (pydantic-settings + .env)
│   │   ├── database.py               # SQLAlchemy + PostgreSQL (prod) / SQLite (local)
│   │   ├── models/                   # Proyecto, Curso, Experiencia, User, Visita, GitHubRepo
│   │   ├── schemas/                  # Validación Pydantic
│   │   ├── routers/                  # API endpoints (CRUD + auth + analytics + contacto + github)
│   │   └── utils/                    # JWT, password hashing (bcrypt directo)
│   ├── create_admin.py               # Script para crear usuario admin inicial
│   ├── render.yaml                   # Configuración de despliegue en Render
│   └── requirements.txt
│
├── .env                              # Variables de entorno (NO en Git)
├── .gitignore                        # Reglas de exclusión para Git
└── readme.md                         # Este archivo
```

---

## Sistema de Analíticas

El tracking de visitas funciona con **`rx.call_script`** ejecutado en el navegador real del visitante:

1. `on_load=State.registrar_visita` en cada página pública dispara `rx.call_script` que recoge datos del navegador
2. El callback `State.enviar_tracking` recibe los datos via websocket y los envía al backend FastAPI con `httpx.post`
3. El backend (`POST /api/analytics/track`) detecta dispositivo, navegador y SO, y almacena la visita
4. El dashboard admin muestra: visitas totales, únicos, visitas/día, dispositivos, SO, navegadores, páginas, referrers y últimas visitas
5. Export a Excel disponible desde el dashboard (con autenticación JWT)

> **Nota:** En Reflex 0.8 (Vite), `rx.script`, `head_components` y `rx.el.script` no funcionan en producción. La única forma fiable es `rx.call_script` con callback.

---

## Diseño Visual

- **Portada**: Foto de perfil con glow animado, nombre, "Python Developer", botones B/N (ES/EN/IT/CA), animaciones escalonadas
- **Navbar**: Glassmorphism (blur + transparencia), links con underline animado al hover
- **Hero**: Foto 180px con borde gradiente, animaciones de entrada
- **Cards**: Bordes `rgba` sutiles, hover con iluminación y elevación, `border-radius: 10px`
- **Contacto**: Layout 2 columnas (info + formulario), iconos en cajas cuadradas
- **Tech stack**: Grid de iconos 90px con hover translateY
- **Paleta**: Negro `#000`, blanco, grises `rgba(255,255,255,0.xx)`

---

## Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Portada — foto, nombre, rol, selector de idioma (ES/EN/IT/CA), animaciones escalonadas |
| `/home` | Página principal con todas las secciones |
| `/cv` | Visor PDF del CV a pantalla completa |
| `/login` | Login admin |
| `/admin` | Dashboard admin |
| `/admin/proyectos` | CRUD proyectos |
| `/admin/cursos` | CRUD cursos |
| `/admin/experiencias` | CRUD experiencias |
| `/admin/analytics` | Dashboard de analíticas |

---

## API Endpoints

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| GET/POST/PUT/DELETE | `/api/proyectos/` | JWT | CRUD proyectos |
| GET/POST/PUT/DELETE | `/api/cursos/` | JWT | CRUD cursos |
| GET/POST/PUT/DELETE | `/api/experiencias/` | JWT | CRUD experiencias |
| POST | `/api/auth/login` | — | Login OAuth2 |
| GET | `/api/auth/me` | JWT | Info usuario actual |
| PUT | `/api/auth/change-password` | JWT | Cambiar contraseña |
| PUT | `/api/auth/change-username` | JWT | Cambiar username |
| GET | `/api/github/repos` | — | Repos GitHub (cache 6h) |
| POST | `/api/contacto/` | — | Enviar email de contacto (Resend) |
| POST | `/api/analytics/track` | — | Registrar visita (público, desde JS) |
| GET | `/api/analytics/resumen` | JWT | Total visitas + únicos (30 días) |
| GET | `/api/analytics/paginas` | JWT | Páginas más visitadas |
| GET | `/api/analytics/dispositivos` | JWT | Dispositivos (desktop/móvil/tablet) |
| GET | `/api/analytics/navegadores` | JWT | Navegadores (Chrome, Firefox, Safari...) |
| GET | `/api/analytics/plataformas` | JWT | Sistemas operativos (Windows, Android, iOS...) |
| GET | `/api/analytics/referrers` | JWT | Origen del tráfico |
| GET | `/api/analytics/visitas-por-dia` | JWT | Visitas agrupadas por día |
| GET | `/api/analytics/recientes` | JWT | Últimas visitas detalladas |
| GET | `/api/analytics/export` | JWT | Exportar a Excel (.xlsx) |

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

# Frontend
cd frontend
pip install -r requirements.txt
reflex init

# Backend
cd ../backend
pip install -r requirements.txt
```

### Configurar `.env`

Crear archivo `.env` en la raíz del proyecto con:

```env
DATABASE_URL=sqlite:///./portfolio.db
SECRET_KEY=tu-clave-secreta
GITHUB_TOKEN=tu-token-github
CORS_ALLOW_ALL=false
RESEND_API_KEY=tu-api-key-resend
CONTACT_EMAIL_TO=tu-email-destino
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

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8001/docs`

### Desplegar cambios a producción

```bash
# Subir cambios (backend se redeploy automáticamente en Render)
git add .
git commit -m "descripcion del cambio"
git push origin main

# Si hay cambios en el frontend, además ejecutar:
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