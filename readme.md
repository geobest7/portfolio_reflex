# Portfolio - Alessandro Febbrai

Portfolio personal full-stack desarrollado con **Reflex** (frontend) y **FastAPI** (backend).

---

## Características

- **Multi-idioma** — ES / EN / IT / CA con traducciones completas
- **Diseño minimalista** — Interfaz negra, limpia y profesional
- **Panel admin** — CRUD completo para proyectos, cursos y experiencias
- **Analíticas propias** — Tracking de visitas, dispositivos y navegadores
- **Formulario de contacto** — Envío de emails real via SMTP
- **Autenticación JWT** — Login seguro para admin
- **GitHub API** — Repositorios cargados automáticamente con cache
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
| **Email** | SMTP (Gmail) |
| **Analytics** | Middleware propio + dashboard admin |
| **Hosting** | Reflex Cloud (frontend) + Render (backend) |
| **Control de versiones** | Git + GitHub |

---

## Despliegue en Producción

| Servicio | Plataforma | URL |
|----------|-----------|-----|
| **Frontend** | Reflex Cloud | `https://portfolio-alessandro-teal-ring.reflex.run` |
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
│   │   ├── states/                   # State unificado
│   │   ├── components/               # Navbar, footer, selectores, skeletons
│   │   ├── sections/                 # Sobre mí, proyectos, formación, experiencia, github, contacto
│   │   ├── pages/                    # Portada, home, CV, login
│   │   └── admin/                    # Dashboard, CRUD proyectos/cursos/experiencias, analíticas
│   ├── assets/                       # CV.pdf, foto_perfil.png, favicon.ico, styles/
│   └── rxconfig.py
│
├── backend/
│   ├── app/
│   │   ├── main.py                   # FastAPI + CORS + middleware analytics + auto-crear admin
│   │   ├── config.py                 # Settings (pydantic-settings + .env)
│   │   ├── database.py               # SQLAlchemy + PostgreSQL (prod) / SQLite (local)
│   │   ├── models/                   # Proyecto, Curso, Experiencia, User, Visita, GitHubRepo
│   │   ├── schemas/                  # Validación Pydantic
│   │   ├── routers/                  # API endpoints (CRUD + auth + analytics + contacto + github)
│   │   ├── middleware/               # Analytics middleware (tracking visitas)
│   │   └── utils/                    # JWT, password hashing (bcrypt directo)
│   ├── create_admin.py               # Script para crear usuario admin inicial
│   ├── render.yaml                   # Configuración de despliegue en Render
│   └── requirements.txt
│
├── .env                              # Variables de entorno (NO en Git)
├── .gitignore                        # Reglas de exclusión para Git
└── README.md                         # Este archivo
```

---

## Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Portada — selector de idioma |
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

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET/POST/PUT/DELETE | `/api/proyectos/` | CRUD proyectos (protegido) |
| GET/POST/PUT/DELETE | `/api/cursos/` | CRUD cursos (protegido) |
| GET/POST/PUT/DELETE | `/api/experiencias/` | CRUD experiencias (protegido) |
| POST | `/api/auth/login` | Login OAuth2 |
| GET | `/api/auth/me` | Info usuario actual |
| PUT | `/api/auth/change-password` | Cambiar contraseña |
| PUT | `/api/auth/change-username` | Cambiar username |
| GET | `/api/github/repos` | Repos GitHub (cache 6h) |
| POST | `/api/contacto/` | Enviar email de contacto |
| GET | `/api/analytics/*` | Estadísticas de visitas (protegido) |

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
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu-email@gmail.com
SMTP_PASSWORD=tu-app-password
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