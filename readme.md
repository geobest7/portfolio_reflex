# 🎨 Mi Portfolio

Portfolio personal desarrollado con **Reflex** (frontend) y **FastAPI** (backend). Proyecto full-stack con sistema multi-idioma, panel de administración, analíticas propias y diseño minimalista.

---

## 📋 Características Planificadas

- 🌍 **Multi-idioma:** Selector de idiomas (ES / EN / IT / CA) con estado global
- 🎭 **Diseño negro minimalista:** Interfaz elegante, limpia y profesional
- 📊 **Panel de administración:** CRUD completo para gestionar contenido
- 📈 **Sistema de analíticas propio:** Tracking de visitas, país, dispositivo, clicks
- 🔐 **Autenticación JWT:** Sistema seguro de login para admin
- 🐙 **Integración GitHub API:** Muestra tus repositorios automáticamente
- 📱 **Responsive design:** Adaptado a móvil, tablet y desktop
- 🎬 **Videos de proyectos:** Showcase visual de tu trabajo
- 📄 **Descarga CV:** Botón para descargar CV en PDF

---

## 🛠️ Stack Tecnológico

**Frontend:**
- **Reflex** - Framework web de Python (genera React por debajo)
- **TailwindCSS** - Estilos utility-first
- **CSS/GSAP** - Animaciones personalizadas

**Backend:**
- **FastAPI** - Framework moderno para APIs
- **SQLAlchemy** - ORM para base de datos
- **PostgreSQL** / **SQLite** - Base de datos (SQLite para dev)
- **JWT** - Autenticación segura
- **Pandas** - Exportación de datos a CSV/Excel
- **Uvicorn** - Servidor ASGI

**DevOps:**
- **Vercel** - Deploy frontend
- **Fly.io / Render** - Deploy backend
- **Git** - Control de versiones

---

## Estructura del Proyecto Explicada

```
mi_portfolio_reflex/
│
├── 📂 frontend/                          # Aplicación Reflex (frontend)
│   ├── mi_portfolio_reflex/             # Paquete principal Python
│   │   ├── __init__.py                  # Convierte la carpeta en paquete Python
│   │   ├── mi_portfolio_reflex.py       # ARCHIVO PRINCIPAL - Define rutas y app (24 líneas)
│   │   ├── state.py                     # Wrapper que importa State desde states/
│   │   ├── translations.py              # Diccionario de traducciones (ES, EN, IT, CA)
│   │   ├── models.py                    # Modelos Pydantic (Proyecto, Curso, Experiencia, GitHubRepo)
│   │   ├── utils.py                     # Funciones helper (convertir_youtube_url)
│   │   │
│   │   ├── states/                      # Estados organizados por responsabilidad
│   │   │   └── __init__.py              # State unificado (736 líneas) - Compatible con Reflex
│   │   │
│   │   ├── components/                  # Componentes reutilizables
│   │   │   ├── __init__.py
│   │   │   ├── selectors.py             # Selectores de idioma
│   │   │   ├── navbar.py                # Navbar con menú hamburguesa
│   │   │   ├── footer.py                # Footer con links sociales
│   │   │   └── skeletons.py             # Skeleton loaders
│   │   │
│   │   ├── sections/                    # Secciones de la página home
│   │   │   ├── __init__.py
│   │   │   ├── sobre_mi.py              # Sección "Sobre mí"
│   │   │   ├── experiencia.py           # Sección "Experiencia"
│   │   │   ├── formacion.py             # Sección "Formación"
│   │   │   ├── proyectos.py             # Sección "Proyectos"
│   │   │   ├── github.py                # Sección "GitHub Repos"
│   │   │   └── contacto.py              # Sección "Contacto"
│   │   │
│   │   ├── pages/                       # Páginas completas
│   │   │   ├── __init__.py
│   │   │   ├── portada.py               # Página portada (/)
│   │   │   ├── home.py                  # Página home (/home)
│   │   │   ├── cv.py                    # Página CV (/cv)
│   │   │   └── login.py                 # Página login (/login)
│   │   │
│   │   └── admin/                       # Panel de administración
│   │       ├── __init__.py
│   │       ├── dashboard.py             # Dashboard admin (/admin)
│   │       ├── proyectos.py             # CRUD proyectos
│   │       ├── cursos.py                # CRUD cursos
│   │       └── experiencias.py          # CRUD experiencias
│   │
│   ├── assets/                          # Archivos estáticos del frontend
│   │   ├── CV.pdf                       # Curriculum Vitae en PDF
│   │   ├── favicon.ico                  # Icono del navegador
│   │   ├── foto_perfil.png              # Foto de perfil circular
│   │   ├── logo.png                     # Logo personalizado
│   │   └── styles/                      # Estilos CSS
│   │       └── styles.css               # CSS personalizado (smooth scroll, responsive)
│   │
│   ├── rxconfig.py                      # CONFIGURACIÓN REFLEX - Puerto 3000, favicon
│   ├── requirements.txt                 # Dependencias Python del frontend
│   ├── .gitignore                       # Ignora .web, __pycache__, .states
│   ├── .web/                            # Archivos generados por Reflex (NO subir a Git)
│   └── .states/                         # Estados de Reflex (NO subir a Git)
│
├── 📂 backend/                           # API FastAPI (backend)
│   ├── app/
│   │   ├── __init__.py                  # Convierte carpeta en paquete Python
│   │   ├── main.py                      # Punto de entrada FastAPI con CORS
│   │   ├── config.py                    # Configuración con pydantic-settings
│   │   ├── database.py                  # Configuración SQLAlchemy + SQLite
│   │   ├── models/                      # Modelos de base de datos
│   │   │   ├── __init__.py
│   │   │   ├── proyecto.py              # Modelo Proyecto (multi-idioma)
│   │   │   ├── curso.py                 # Modelo Curso/Diploma (multi-idioma)
│   │   │   ├── experiencia.py           # Modelo Experiencia
│   │   │   ├── user.py                  # Modelo User (autenticación)
│   │   │   └── github_repo.py           # Modelo GitHubRepo (cache)
│   │   ├── schemas/                     # Schemas Pydantic para validación
│   │   │   ├── __init__.py
│   │   │   ├── proyecto.py              # Schemas Proyecto
│   │   │   ├── curso.py                 # Schemas Curso
│   │   │   ├── experiencia.py           # Schemas Experiencia
│   │   │   └── auth.py                  # Schemas Auth (UserLogin, Token, etc)
│   │   ├── routers/                     # Endpoints API (CRUD completo)
│   │   │   ├── __init__.py
│   │   │   ├── proyectos.py             # Endpoints /api/proyectos (protegidos)
│   │   │   ├── cursos.py                # Endpoints /api/cursos (protegidos)
│   │   │   ├── experiencias.py          # Endpoints /api/experiencias (protegidos)
│   │   │   ├── auth.py                  # Endpoints /api/auth (login, me, register)
│   │   │   └── github.py                # Endpoints /api/github (repos con cache)
│   │   └── utils/                       # Utilidades
│   │       └── auth.py                  # JWT, password hashing, dependencies
│   │
│   ├── seed_data.py                     # Script para poblar la base de datos
│   ├── create_admin.py                  # Script para crear usuario admin
│   ├── portfolio.db                     # Base de datos SQLite (desarrollo)
│   └── requirements.txt                 # Dependencias Python del backend
│
├── 📂 assets/                            # Archivos estáticos globales (vacio)
│
├── 📂 venv/                              # Entorno virtual Python (NO se sube a Git)
│
├── .env                                  # VARIABLES DE ENTORNO - Contraseñas, API keys
├── .gitignore                           # Archivos que Git debe ignorar
├── ARQUITECTURA.md                      # Documentación de arquitectura del proyecto
├── README.md                            # Este archivo - Documentación del proyecto
└── PROGRESO_DIARIO.md                  # Tracking del avance (solo Día 9)

---

## Descripción de Archivos Clave

### **Archivos de Configuración**

#### `.env`
**Qué es:** Archivo con variables de entorno sensibles (contraseñas, tokens).  
**Para qué sirve:** Guardar información secreta que NO debe subirse a Git.  
**Contenido:**
- `DATABASE_URL` - URL de conexión a la base de datos
- `SECRET_KEY` - Clave secreta para JWT
- `GITHUB_TOKEN` - Token para API de GitHub (opcional)

⚠️ **NUNCA subir este archivo a Git**

---

#### `.gitignore`
**Qué es:** Lista de archivos/carpetas que Git ignorará.  
**Para qué sirve:** Evitar subir archivos sensibles, temporales o pesados.  
**Incluye:**
- `venv/` - Entorno virtual (cada dev tiene el suyo)
- `.env` - Variables secretas
- `__pycache__/` - Cache de Python
- `*.db` - Base de datos local

---

#### `frontend/rxconfig.py`
**Qué es:** Archivo de configuración de Reflex.  
**Para qué sirve:** Define el nombre de la app y configuraciones globales.  
**Configuración actual:**
```python
app_name = "mi_portfolio_reflex"  # Debe coincidir con el nombre de la carpeta
port = 3000                        # Puerto donde corre la app
```

---

#### `frontend/requirements.txt`
**Qué es:** Lista de dependencias Python del frontend.  
**Para qué sirve:** `pip install -r requirements.txt` instala todo lo necesario.  
**Contiene:**
- `reflex>=0.4.0` - Framework web

---

#### `backend/requirements.txt`
**Qué es:** Lista de dependencias Python del backend.  
**Para qué sirve:** Instalar todas las librerías necesarias para la API.  
**Contiene:**
- `fastapi` - Framework de API
- `uvicorn` - Servidor ASGI
- `sqlalchemy` - ORM para bases de datos
- `python-jose` - JWT para autenticación
- `passlib` - Hash de contraseñas
- `pandas` - Exportar datos a Excel/CSV
- `requests` - Llamadas a APIs externas (GitHub)

---

### Archivos de Código

#### `frontend/mi_portfolio_reflex/mi_portfolio_reflex.py`
**Qué es:** Archivo principal de la aplicación Reflex.  
**Para qué sirve:** Define las páginas, componentes y rutas de tu portfolio.  

**Contenido actual:**
**Componentes Públicos:**
- `selector_idioma_portada()` - Selector con redirección a /home
- `selector_idioma()` - Selector sin redirección para navbar
- `navbar()` - Barra de navegación sticky con links traducidos
- `seccion_sobre_mi()` - Sección "Sobre mí" con descripción y badges
- `skeleton_proyecto/curso/experiencia()` - Skeleton loaders para carga
- `card_proyecto/curso/experiencia()` - Cards dinámicas con animaciones
- `seccion_proyectos()` - Proyectos dinámicos desde API
- `seccion_formacion()` - Cursos dinámicos desde API
- `seccion_experiencia()` - Experiencias dinámicas desde API
- `seccion_github()` - Repositorios GitHub con cache
- `seccion_contacto()` - Información + formulario traducido
- `footer()` - Footer con links sociales

**Páginas Públicas:**
- `portada()` - Página inicial (ruta `/`)
- `home()` - Página principal con todas las secciones (ruta `/home`)
- `pagina_cv()` - Visor PDF a pantalla completa (ruta `/cv`)

**Autenticación:**
- `pagina_login()` - Formulario de login OAuth2 (ruta `/login`)
- `dashboard_admin()` - Dashboard protegido con cards de navegación (ruta `/admin`)

**Panel Admin - CRUD Proyectos:**
- `admin_proyectos()` - Listado con tabla y botones de acción (ruta `/admin/proyectos`)
- `formulario_proyecto()` - Crear/editar proyecto multi-idioma (ruta `/admin/proyectos/form`)

**Panel Admin - CRUD Cursos:**
- `admin_cursos()` - Listado con tabla y botones de acción (ruta `/admin/cursos`)
- `formulario_curso()` - Crear/editar curso multi-idioma (ruta `/admin/cursos/form`)

**Panel Admin - CRUD Experiencias:**
- `admin_experiencias()` - Listado con tabla y botones de acción (ruta `/admin/experiencias`)
- `formulario_experiencia()` - Crear/editar experiencia multi-idioma (ruta `/admin/experiencias/form`)

- `app = rx.App()` - Inicialización con CSS personalizado
- Registro de 11 rutas con `app.add_page()`

---

#### `frontend/mi_portfolio_reflex/__init__.py`
**Qué es:** Archivo que convierte la carpeta en un paquete Python.  
**Para qué sirve:** Permite que Python importe módulos desde esta carpeta.  
**Contenido:** Vacío (por ahora)

---

#### `backend/app/__init__.py` (y otros `__init__.py`)
**Qué es:** Igual que el anterior, marca carpetas como paquetes Python.  
**Para qué sirve:** Estructura modular del código.

---

### Archivos de Documentación

#### `README.md`
**Qué es:** Este archivo que estás leyendo.  
**Para qué sirve:** Documentación general del proyecto para desarrolladores.

---

#### `PROGRESO_DIARIO.md`
**Qué es:** Archivo temporal de tracking.  
**Para qué sirve:** Registrar qué se hizo cada día y qué falta por hacer.  
**Se borrará:** Al finalizar el proyecto.

---

## Estructura Detallada de las Páginas

### Página 1: Portada (`/`)

**Ruta:** `http://localhost:3000/`

**Propósito:** Página de bienvenida donde el usuario selecciona su idioma preferido.

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│         (Centrado vertical)         │
│                                     │
│      Alessandro Febbrai             │  ← Heading size 9, blanco
│                                     │
│   Select language / Selecciona      │  ← Texto gris (#808080)
│           idioma                    │
│                                     │
│    [ES] [EN] [IT] [CA]             │  ← Botones horizontales
│                                     │
│         (Centrado vertical)         │
│                                     │
└─────────────────────────────────────┘
```

**Componentes (de arriba a abajo):**
1. **rx.heading** - Nombre "Alessandro Febbrai"
   - Tamaño: `size="9"` (muy grande)
   - Color: Blanco
   - Posición: Centrado

2. **rx.text** - Texto "Select language / Selecciona idioma"
   - Tamaño: `size="3"` (pequeño)
   - Color: Gris `#808080`
   - Posición: Centrado debajo del nombre

3. **selector_idioma_portada()** - 4 botones de idioma
   - Disposición: Horizontal (`rx.hstack`)
   - Botones: ES, EN, IT, CA
   - Funcionalidad: Al hacer clic, cambia idioma y redirige a `/home`
   - Estilo: Fondo blanco para idioma activo, gris para inactivos

**Características:**
- Fondo negro puro (`#000000`)
- Todo centrado vertical y horizontalmente
- Altura mínima: 100vh (pantalla completa)
- Sin navbar ni otros elementos

---

### Página 2: Home (`/home`)

**Ruta:** `http://localhost:3000/home`

**Propósito:** Página principal con contenido del portfolio traducido.

**Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  AF  Inicio  Sobre mí  Proyectos  Contacto  CV  [ES]  │  ← Navbar (horizontal)
├─────────────────────────────────────────────────────────┤
│                    SECCIÓN HERO                         │
│         ¡Hola! Soy Alessandro Febbrai                  │  ← Título
│              Desarrollador Python                       │  ← Subtítulo
│           Estudiando programación                       │  ← Descripción
├─────────────────────────────────────────────────────────┤
│                  SECCIÓN SOBRE MÍ                       │
│                    Sobre mí                             │  ← Título
│         Descripción personal detallada...               │  ← Texto
│                  Habilidades                            │  ← Subtítulo
│    [Python] [Reflex] [FastAPI] [JavaScript] [Git]     │  ← Badges
├─────────────────────────────────────────────────────────┤
│                 SECCIÓN PROYECTOS                       │
│                   Proyectos                             │  ← Título
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │Proyecto 1│  │Proyecto 2│  │Proyecto 3│            │  ← 3 Cards
│  │  Desc... │  │  Desc... │  │  Desc... │            │
│  │[Ver código]│ │[Ver código]│ │[Ver código]│         │
│  └──────────┘  └──────────┘  └──────────┘            │
├─────────────────────────────────────────────────────────┤
│                 SECCIÓN CONTACTO                        │
│                   Contacto                              │  ← Título
│          Información de contacto                        │  ← Subtítulo
│    📧 Email: alessandro.febbrai@ejemplo.com            │
│    📱 Teléfono: +34 XXX XXX XXX                        │
│    💼 LinkedIn: /alessandro-febbrai                     │
│    🐙 GitHub: /geobest7                                │
│      ¿Tienes un proyecto en mente? ¡Hablemos!         │  ← Subtítulo form
│              [Input: Nombre]                            │
│              [Input: Email]                             │
│              [TextArea: Mensaje]                        │
│              [Enviar mensaje]                           │  ← Botón
├─────────────────────────────────────────────────────────┤
│                     FOOTER                              │
│          🐙 GitHub  💼 LinkedIn  📧 Email              │  ← Links sociales
│         © 2026 Alessandro Febbrai                       │  ← Copyright
└─────────────────────────────────────────────────────────┘
```

**Componentes (de arriba a abajo):**

1. **navbar()** - Barra de navegación superior
   - Disposición: Horizontal (`rx.hstack`)
   - Elementos de izquierda a derecha:
     - Logo "AF" (heading size 7)
     - Spacer (espacio flexible)
     - Links: Inicio, Sobre mí, Proyectos, Contacto, CV (horizontal)
     - Spacer (espacio flexible)
     - Selector de idioma (4 botones horizontales)
   - Fondo: Negro `#000000`
   - Padding: `1em 2em`
   - Ancho: 100%
   - Posición: Fixed (sticky)

2. **rx.vstack** - Contenido hero (vertical)
   - **rx.heading** - Título traducido (ej: "¡Hola! Soy Alessandro Febbrai")
     - Tamaño: `size="9"` (muy grande)
     - Color: Blanco (heredado)
   
   - **rx.text** - Subtítulo traducido (ej: "Desarrollador Python")
     - Tamaño: `size="5"` (mediano)
     - Color: Blanco (heredado)
   
   - Padding: `4em 2em`
   - Padding-top: `6em` (compensar navbar sticky)
   - ID: `"inicio"` (para smooth scroll)

**Características:**
- Fondo negro puro (`#000000`)
- Texto blanco en toda la página
- Navbar fija en la parte superior
- Contenido hero con padding `4em 2em`
- Spacing vertical entre elementos: `4`
- Altura mínima: 100vh (pantalla completa)
- Todo el contenido es reactivo y cambia según el idioma seleccionado

---

### Página 3: CV (`/cv`)

**Ruta:** `http://localhost:3000/cv`

**Propósito:** Visualizar el CV en formato PDF a pantalla completa.

**Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  AF    Inicio  Sobre mí  Proyectos  Contacto  CV  [ES] │  ← Navbar
├─────────────────────────────────────────────────────────┤
│                                                         │
│                                                         │
│                    [PDF VIEWER]                         │
│              Curriculum Vitae completo                  │
│                 a pantalla completa                     │
│                                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Componentes:**
1. **navbar()** - Barra de navegación (igual que en /home)
2. **rx.html con iframe** - Visor PDF a pantalla completa
   - Archivo: `/CV.pdf` (servido desde `frontend/assets/`)
   - Posición: `absolute` para ocupar toda la altura
   - Altura: `calc(100% - 4em)` (pantalla completa menos navbar)
   - Sin bordes

**Características:**
- PDF ocupa toda la pantalla disponible
- Navbar permite navegar de vuelta a otras secciones
- Diseño minimalista sin distracciones
- El usuario puede usar el visor PDF nativo del navegador para descargar

---

## Instalación y Uso

### Requisitos Previos
- Python 3.9 o superior
- pip (gestor de paquetes Python)
- Git (opcional)

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd mi_portfolio_reflex
```

### 2. Crear y activar entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias del Frontend
```bash
cd frontend
pip install -r requirements.txt
reflex init
```

### 4. Instalar dependencias del Backend
```bash
cd ../backend
pip install -r requirements.txt
```

### 5. Configurar variables de entorno
Edita el archivo `.env` en la raíz con tus configuraciones.

### 6. Ejecutar la aplicación

**Frontend (Reflex):**
```bash
cd frontend
reflex run
```
La app estará en: `http://localhost:3000`

**Backend (FastAPI):**
```bash
cd backend
uvicorn app.main:app --reload --port 8001
```
La API estará en: `http://localhost:8001/docs`

---

## 📊 Estado del Proyecto

### ✅ Completado (14 Enero 2026):

**Fase 1 - Setup Inicial** ✅
- Estructura de carpetas completa
- Entorno virtual y dependencias
- Configuración de Reflex

**Fase 2 - Sistema Multi-idioma** ✅
- 4 idiomas funcionando: ES, EN, IT, CA
- Selector de idioma reactivo
- 100+ traducciones implementadas

**Fase 3 - Frontend (95% completado)** ✅
- ✅ Página Portada con selector de idioma
- ✅ Página Home con todas las secciones
- ✅ Página CV con visor PDF
- ✅ Navbar sticky con menú hamburguesa responsive
- ✅ Logo personalizado y favicon
- ✅ Sección Hero con foto de perfil circular
- ✅ Sección Sobre mí (descripción, experiencia actual, badges de habilidades)
- ✅ Sección Formación (diploma + 3 cursos)
- ✅ Sección Proyectos (3 cards - pendiente dinamizar con DB)
- ✅ Sección Contacto (información + formulario traducido)
- ✅ Footer con links sociales
- ✅ Responsive design completo (móvil, tablet, desktop)
- ✅ Smooth scroll entre secciones
- ✅ Formulario de contacto con validación multi-idioma
- ✅ Fix: limpieza de formulario al navegar

**Fase 4 - Backend con FastAPI** ✅ (14 Enero 2026)
- ✅ Setup FastAPI + SQLAlchemy + SQLite
- ✅ Configuración con pydantic-settings y CORS
- ✅ Modelos: Proyecto, Curso, Experiencia (multi-idioma)
- ✅ Schemas Pydantic para validación
- ✅ Endpoints CRUD completos (GET, POST, PUT, DELETE)
- ✅ Soft delete implementado
- ✅ Seed data con 3 proyectos, 4 cursos, 1 experiencia
- ✅ API funcionando en http://localhost:8001
- ✅ Documentación Swagger UI en /docs
- ✅ Base de datos SQLite creada y poblada

**Fase 5 - Integración Frontend-Backend** ✅ (15 Enero 2026)
- ✅ Instalado httpx>=0.24.0 en frontend
- ✅ Clases Pydantic (Proyecto, Curso) en state.py
- ✅ Funciones cargar_proyectos() y cargar_cursos() con HTTP requests
- ✅ Sección Proyectos dinamizada (datos desde API)
- ✅ Sección Formación dinamizada (datos desde API)
- ✅ Multi-idioma funcionando con datos dinámicos
- ✅ Loading states y error handling implementados
- ✅ Manejo de valores None de la API
- ✅ Backend en puerto 8001, Frontend en puerto 3000

**Fase 6 - Optimizaciones y Mejoras** ✅ (17 Enero 2026)
- ✅ Auto-carga de datos al entrar a /home (sin botones manuales)
- ✅ Sección Experiencia laboral dinámica desde API
- ✅ Cache simple: solo carga datos si las listas están vacías
- ✅ Traducciones multi-idioma para sección Experiencia
- ✅ Link "Experiencia" en navbar (desktop y móvil)
- ✅ Eliminada subsección de experiencia estática duplicada
- ✅ 3 secciones dinámicas funcionando: Proyectos, Formación, Experiencia
- ✅ Skeleton loaders para proyectos, cursos y experiencias
- ✅ Animaciones fade-in-up para cards dinámicas
- ✅ Integración GitHub API con cache de 6 horas
- ✅ Sección GitHub dinámica en /home con repositorios reales
- ✅ Link "GitHub" en navbar

**Fase 7 - Autenticación y Seguridad** ✅ (17 Enero 2026)
- ✅ Sistema de autenticación JWT con python-jose
- ✅ Modelo User con campos: username, email, hashed_password, is_admin
- ✅ Hash de contraseñas con passlib[bcrypt]
- ✅ Router /api/auth con endpoints: login, me, register
- ✅ Script create_admin.py para crear usuario administrador inicial
- ✅ Protección de endpoints CRUD (solo admin puede POST/PUT/DELETE)
- ✅ Página /login con formulario OAuth2
- ✅ Dashboard /admin con protección de ruta
- ✅ Estado de autenticación en frontend (token, usuario, login/logout)

**Fase 8 - Panel Admin CRUD Completo** ✅ (17-18 Enero 2026)
- ✅ **CRUD Proyectos:** State con funciones (cargar, crear, editar, eliminar)
- ✅ Página /admin/proyectos con tabla y botones de acción
- ✅ Formulario /admin/proyectos/form para crear/editar (multi-idioma)
- ✅ **CRUD Cursos:** State, listado y formulario completos
- ✅ Página /admin/cursos con gestión completa
- ✅ Formulario /admin/cursos/form con campos multi-idioma
- ✅ **CRUD Experiencias:** State, listado y formulario completos
- ✅ Página /admin/experiencias con tabla de gestión
- ✅ Formulario /admin/experiencias/form con todos los campos
- ✅ Modelo Curso actualizado con institucion_es/en/it/ca
- ✅ Base de datos recreada con estructura multi-idioma completa
- ✅ Todas las operaciones CRUD funcionando correctamente
- ✅ **Videos YouTube embebidos:** Proyectos y Experiencias pueden incluir video_url
- ✅ Conversión automática de URLs YouTube a formato embed

**Fase 9 - Limpieza y Seguridad** ✅ (3 Febrero 2026)
- ✅ Eliminado `hero_descripcion` redundante (simplificación del Hero)
- ✅ SECRET_KEY movida a configuración centralizada (config.py → .env)
- ✅ Endpoints para cambiar credenciales del admin:
  - PUT /api/auth/change-password
  - PUT /api/auth/change-username
- ✅ Validación de contraseñas (mínimo 6 caracteres)
- ✅ Validación de usernames (mínimo 3 caracteres)
- ✅ Documentación actualizada

### ⏳ Pendiente:

**Fase 9 - Sistema de Analíticas**
**Fase 10 - SEO y Optimización**
**Fase 11 - Despliegue en Producción**

Ver `PROGRESO_DIARIO.md` y `ARQUITECTURA.md` para documentación completa.

---

## 🧪 Testing
(Por implementar en fases posteriores)

---

## 🚢 Despliegue

(Por implementar en Fase 10)

**Frontend:** Vercel  

---

## 📝 Notas de Desarrollo

- Siempre trabajar con el entorno virtual activado
- El frontend corre en puerto 3000
- El backend corre en puerto 8001
- La base de datos en desarrollo es SQLite (local)
- Para producción se usará PostgreSQL

---

## 🤝 Contribución

Proyecto personal en desarrollo.

---

## 📄 Licencia

Todos los derechos reservados - Proyecto personal

---

## 👤 Autor

Alessandro Febbrai 

---

**Última actualización:** 3 Febrero 2026 (limpieza de código, mejoras de seguridad admin)