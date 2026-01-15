# PROGRESO DIARIO DEL PROYECTO PORTFOLIO

> Archivo para trackear el progreso dia a dia del desarrollo del portfolio.

---

## Dia 9 (14 Enero 2026) - Backend FastAPI Implementado

### Objetivo: Implementar backend completo con FastAPI

**Logros de la sesion:**

#### 1. Configuracion Base del Backend
- Creado backend/app/config.py con pydantic-settings
- Creado backend/app/database.py con SQLAlchemy + SQLite
- Creado backend/app/main.py con FastAPI + CORS configurado
- Variables de entorno para desarrollo y produccion
- Dependency injection para sesiones de base de datos

#### 2. Modelos de Base de Datos (SQLAlchemy)
- backend/app/models/proyecto.py - Modelo Proyecto con multi-idioma
  - Campos: titulo_*, descripcion_* (es, en, it, ca)
  - Tecnologias (JSON), URLs (GitHub, demo), imagen
  - Flags: destacado, activo, orden
- backend/app/models/curso.py - Modelo Curso/Diploma
  - Tipo: curso o diploma
  - Campos multi-idioma, institucion, fechas
  - Certificado URL, orden, activo
- backend/app/models/experiencia.py - Modelo Experiencia
  - Tipo, empresa, cargo multi-idioma
  - Fechas (inicio, fin, actual)
  - Tecnologias (JSON), mostrar_en_web, orden

#### 3. Schemas Pydantic (Validacion)
- backend/app/schemas/proyecto.py - ProyectoBase, Create, Update, Response
- backend/app/schemas/curso.py - CursoBase, Create, Update, Response
- backend/app/schemas/experiencia.py - ExperienciaBase, Create, Update, Response
- Validacion automatica de tipos y campos requeridos
- Serializacion con from_attributes = True

#### 4. Routers con CRUD Completo

**backend/app/routers/proyectos.py:**
- GET /api/proyectos/ - Listar proyectos (con filtro destacados)
- GET /api/proyectos/{id} - Obtener proyecto por ID
- POST /api/proyectos/ - Crear proyecto
- PUT /api/proyectos/{id} - Actualizar proyecto
- DELETE /api/proyectos/{id} - Eliminar proyecto (soft delete)

**backend/app/routers/cursos.py:**
- GET /api/cursos/ - Listar cursos
- GET /api/cursos/{id} - Obtener curso por ID
- POST /api/cursos/ - Crear curso
- PUT /api/cursos/{id} - Actualizar curso
- DELETE /api/cursos/{id} - Eliminar curso (soft delete)

**backend/app/routers/experiencias.py:**
- GET /api/experiencias/ - Listar experiencias (con filtro mostrar_en_web)
- GET /api/experiencias/{id} - Obtener experiencia por ID
- POST /api/experiencias/ - Crear experiencia
- PUT /api/experiencias/{id} - Actualizar experiencia
- DELETE /api/experiencias/{id} - Eliminar experiencia (soft delete)

#### 5. Seed Data y Base de Datos
- Creado backend/seed_data.py para poblar la base de datos
- 3 proyectos de ejemplo (Portfolio, Task Manager, E-commerce API)
- 4 cursos/diplomas (Python, FastAPI, Git, Diploma Tecnico)
- 1 experiencia (Practicas en Tech Solutions)
- Todos los datos en 4 idiomas (ES, EN, IT, CA)
- Base de datos SQLite creada: backend/portfolio.db

#### 6. Funcionalidades Implementadas
- Soft Delete: Campo activo en todos los modelos
- Ordenamiento: Campo orden para controlar visualizacion
- Filtros: destacados, mostrar_en_web, activo
- CORS: Configurado para frontend (localhost:3000)
- Documentacion automatica: Swagger UI en /docs
- Health check: Endpoint /health
- Multi-idioma: Todos los textos en 4 idiomas

#### 7. Dependencias Anadidas
- pydantic-settings>=2.0.0 anadido a requirements.txt
- FastAPI, SQLAlchemy, Uvicorn ya estaban instalados

### API Funcionando
- URL: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health
- Puerto: 8000 (backend) | 3000 (frontend)

### Estructura Final del Backend
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app principal
│   ├── config.py            # Settings y configuracion
│   ├── database.py          # SQLAlchemy setup
│   ├── models/
│   │   ├── __init__.py
│   │   ├── proyecto.py      # Modelo Proyecto
│   │   ├── curso.py         # Modelo Curso
│   │   └── experiencia.py   # Modelo Experiencia
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── proyecto.py      # Schemas Proyecto
│   │   ├── curso.py         # Schemas Curso
│   │   └── experiencia.py   # Schemas Experiencia
│   └── routers/
│       ├── __init__.py
│       ├── proyectos.py     # Endpoints Proyectos
│       ├── cursos.py        # Endpoints Cursos
│       └── experiencias.py  # Endpoints Experiencias
├── seed_data.py             # Script para poblar DB
├── requirements.txt         # Dependencias
└── portfolio.db             # Base de datos SQLite
```

### Proximos Pasos (Sesion 10)
1. Integrar frontend con backend (fetch data desde API)
2. Reemplazar datos hardcoded por llamadas a la API
3. Loading states en frontend
4. Error handling
5. Opcional: GitHub API integration para repos dinamicos

### Commits de la Sesion
1. Implementar backend FastAPI con CRUD completo
2. Actualizar README.md con Fase 4 backend completada
3. Corregir PROGRESO_DIARIO.md sin caracteres especiales

### Notas Tecnicas
- Soft delete: Los registros no se eliminan fisicamente, solo se marca activo=False
- Multi-idioma: Cada modelo tiene campos *_es, *_en, *_it, *_ca
- JSON fields: Tecnologias se guardan como JSON array
- Fechas: Usando date de Python para fecha_inicio/fecha_fin
- Validacion: Pydantic valida automaticamente tipos y campos requeridos
- CORS: Configurado para permitir requests desde localhost:3000

---

## Dia 10 (15 Enero 2026) - Integracion Frontend-Backend Completada

### Objetivo: Conectar frontend Reflex con backend FastAPI

**Logros de la sesion:**

#### 1. Configuracion de Dependencias
- Instalado httpx>=0.24.0 en frontend/requirements.txt
- Configurado backend para correr en puerto 8001
- Frontend en puerto 3000, backend en puerto 8001

#### 2. Clases Pydantic en Frontend
- Creadas clases Proyecto y Curso en state.py
- Campos multi-idioma: titulo_*, descripcion_* (es, en, it, ca)
- Manejo de campos opcionales (github_url, demo_url, certificado_url)
- Validacion automatica con Pydantic

#### 3. Funciones de Carga de Datos
- cargar_proyectos() - Fetch desde http://localhost:8001/api/proyectos/
- cargar_cursos() - Fetch desde http://localhost:8001/api/cursos/
- Conversion de None a string vacio para campos opcionales
- Manejo de errores con try/except
- Loading states (cargando_proyectos, cargando_cursos)
- Mensajes de error descriptivos

#### 4. Dinamizacion de Secciones
- Seccion Proyectos: Datos dinamicos desde API
  - rx.foreach para iterar sobre State.proyectos
  - Acceso a atributos con notacion de punto (proyecto.titulo_es)
  - Multi-idioma con rx.cond anidados
  - Links condicionales (github_url, demo_url)
- Seccion Formacion: Datos dinamicos desde API
  - rx.foreach para iterar sobre State.cursos
  - Diferenciacion visual diploma vs curso (colores)
  - Link condicional a certificado
  - Fechas con formato "inicio - fin" o "inicio - Actualidad"

#### 5. Solucion de Problemas Tecnicos
- Error de tipos con Optional[str] en Pydantic
- Solucion: Cambiar a str = "" sin Optional
- Error con rx.link y href con valores None
- Solucion: Convertir None a "" antes de crear objetos Pydantic
- Error con notacion de diccionario en rx.foreach
- Solucion: Usar notacion de atributos (objeto.campo)

### Funcionalidades Implementadas
- Carga dinamica de 3 proyectos desde API
- Carga dinamica de 4 cursos/diplomas desde API
- Multi-idioma funcionando con datos de la API
- Spinners de carga mientras se obtienen datos
- Mensajes de error si falla la conexion
- Links externos a GitHub, demos y certificados

### Estructura de Integracion
```
Frontend (Reflex - Puerto 3000)
    |
    | HTTP GET requests (httpx)
    |
    v
Backend (FastAPI - Puerto 8001)
    |
    | SQLAlchemy queries
    |
    v
Base de Datos (SQLite - portfolio.db)
```

### Proximos Pasos (Sesion 11)
1. Auto-carga de datos al entrar a la pagina (sin botones)
2. Seccion Experiencia laboral dinamizada
3. Cache de datos para evitar recargas
4. Skeleton loaders en lugar de spinners
5. Integracion GitHub API para repos dinamicos

### Commits de la Sesion
1. Integrar frontend con backend FastAPI - Secciones dinamicas
2. Actualizar documentacion - Sesion 10 completada

### Notas Tecnicas
- httpx para requests HTTP asincronos
- Pydantic para validacion de datos del API
- rx.foreach para renderizado dinamico de listas
- rx.cond para condicionales en UI
- Manejo de None: if valor is None: valor = ""
- Backend y frontend en puertos diferentes para evitar conflictos

---

**Ultima actualizacion:** 15 Enero 2026
