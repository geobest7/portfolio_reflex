# 🎨 Mi Portfolio

Portfolio personal desarrollado con **Reflex** (frontend) y **FastAPI** (backend). Proyecto full-stack con sistema multi-idioma, panel de administración, analíticas propias y diseño minimalista.

---

## 📋 Características Planificadas

- 🌍 **Multi-idioma:** Selector de idiomas (ES / EN / IT / CA) con estado global
- 🎭 **Diseño negro minimalista:** Interfaz elegante y moderna
- ✨ **Efecto lettering animado:** Animación del nombre en la portada
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

## 📁 Estructura del Proyecto Explicada

```
mi_portfolio_reflex/
│
├── 📂 frontend/                          # Aplicación Reflex (frontend)
│   ├── mi_portfolio_reflex/             # Paquete principal Python
│   │   ├── __init__.py                  # Convierte la carpeta en paquete Python
│   │   ├── mi_portfolio_reflex.py       # 🔴 ARCHIVO PRINCIPAL - Define páginas y app
│   │   ├── state.py                     # (futuro) Estado global: idiomas, datos compartidos
│   │   ├── components/                  # Componentes reutilizables (navbar, cards, etc)
│   │   ├── pages/                       # Páginas separadas (home, projects, admin)
│   │   └── styles/                      # Archivos CSS personalizados
│   │
│   ├── rxconfig.py                      # 🔴 CONFIGURACIÓN REFLEX - Puerto, nombre app
│   └── requirements.txt                 # Dependencias Python del frontend
│
├── 📂 backend/                           # API FastAPI (backend)
│   └── app/
│       ├── __init__.py                  # Convierte carpeta en paquete Python
│       ├── main.py                      # (futuro) Punto de entrada FastAPI
│       ├── database.py                  # (futuro) Configuración de base de datos
│       ├── auth.py                      # (futuro) Sistema de autenticación JWT
│       ├── models/                      # Modelos de base de datos (tablas)
│       │   └── __init__.py
│       └── routers/                     # Endpoints API organizados por recurso
│           └── __init__.py
│   └── requirements.txt                 # Dependencias Python del backend
│
├── 📂 assets/                            # Archivos estáticos
│   ├── images/                          # Fotos personales, logos, iconos
│   ├── videos/                          # Videos demo de proyectos
│   └── cv/                              # Archivos CV para descarga
│
├── 📂 venv/                              # Entorno virtual Python (NO se sube a Git)
│
├── .env                                  # 🔴 VARIABLES DE ENTORNO - Contraseñas, API keys
├── .gitignore                           # Archivos que Git debe ignorar
├── README.md                            # 📖 Este archivo - Documentación del proyecto
└── PROGRESO_DIARIO.md                  # 📊 Tracking temporal del avance día a día

```

---

## 📄 Descripción de Archivos Clave

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

### **Archivos de Código**

#### `frontend/mi_portfolio_reflex/mi_portfolio_reflex.py`
**Qué es:** Archivo principal de la aplicación Reflex.  
**Para qué sirve:** Define las páginas, componentes y rutas de tu portfolio.  
**Contenido actual:**
- Función `index()` que retorna la página principal
- `app = rx.App()` crea la aplicación
- `app.add_page(index)` registra la página

**Próximos pasos:** Aquí añadiremos el selector de idiomas, navbar, portada, secciones, etc.

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

### **Archivos de Documentación**

#### `README.md`
**Qué es:** Este archivo que estás leyendo.  
**Para qué sirve:** Documentación general del proyecto para desarrolladores.

---

#### `PROGRESO_DIARIO.md`
**Qué es:** Archivo temporal de tracking.  
**Para qué sirve:** Registrar qué se hizo cada día y qué falta por hacer.  
**Se borrará:** Al finalizar el proyecto.

---

## 🚀 Instalación y Uso

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

**Backend (FastAPI) - Cuando esté implementado:**
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```
La API estará en: `http://localhost:8000/docs`

---

## 📊 Estado del Proyecto

**Fase actual:** ✅ Fase 1 - Setup inicial completado (11/12/2025)

Ver `PROGRESO_DIARIO.md` para el tracking detallado del avance.

---

## 🧪 Testing

(Por implementar en fases posteriores)

---

## 🚢 Despliegue

(Por implementar en Fase 10)

**Frontend:** Vercel  
**Backend:** Fly.io / Render / Railway  
**Base de datos:** PostgreSQL en producción

---

## 📝 Notas de Desarrollo

- Siempre trabajar con el entorno virtual activado
- El frontend corre en puerto 3000
- El backend correrá en puerto 8000
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

**Última actualización:** 11 Diciembre 2025