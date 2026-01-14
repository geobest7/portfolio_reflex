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

**Ultima actualizacion:** 14 Enero 2026
