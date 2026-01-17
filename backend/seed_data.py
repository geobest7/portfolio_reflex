from datetime import date
from app.database import SessionLocal, engine, Base
from app.models.proyecto import Proyecto
from app.models.curso import Curso
from app.models.experiencia import Experiencia

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    try:
        # Limpiar datos existentes
        db.query(Proyecto).delete()
        db.query(Curso).delete()
        db.query(Experiencia).delete()
        
        # PROYECTOS
        proyectos = [
            Proyecto(
                titulo_es="Portfolio Personal con Reflex",
                titulo_en="Personal Portfolio with Reflex",
                titulo_it="Portfolio Personale con Reflex",
                titulo_ca="Portfolio Personal amb Reflex",
                descripcion_es="Portfolio web desarrollado con Reflex (Python) y FastAPI para el backend. Incluye sistema multi-idioma, formulario de contacto y gestión dinámica de contenido.",
                descripcion_en="Web portfolio developed with Reflex (Python) and FastAPI for the backend. Includes multi-language system, contact form and dynamic content management.",
                descripcion_it="Portfolio web sviluppato con Reflex (Python) e FastAPI per il backend. Include sistema multi-lingua, modulo di contatto e gestione dinamica dei contenuti.",
                descripcion_ca="Portfolio web desenvolupat amb Reflex (Python) i FastAPI per al backend. Inclou sistema multi-idioma, formulari de contacte i gestió dinàmica de contingut.",
                tecnologias=["Python", "Reflex", "FastAPI", "SQLAlchemy", "SQLite"],
                url_github="https://github.com/geobest7/portfolio_reflex",
                url_demo=None,
                imagen_url=None,
                destacado=True,
                orden=1,
                activo=True
            ),
            Proyecto(
                titulo_es="Sistema de Gestión de Tareas",
                titulo_en="Task Management System",
                titulo_it="Sistema di Gestione Attività",
                titulo_ca="Sistema de Gestió de Tasques",
                descripcion_es="Aplicación web para gestionar tareas y proyectos con autenticación de usuarios.",
                descripcion_en="Web application to manage tasks and projects with user authentication.",
                descripcion_it="Applicazione web per gestire attività e progetti con autenticazione utenti.",
                descripcion_ca="Aplicació web per gestionar tasques i projectes amb autenticació d'usuaris.",
                tecnologias=["Python", "Django", "PostgreSQL", "Bootstrap"],
                url_github="https://github.com/geobest7/task-manager",
                url_demo=None,
                imagen_url=None,
                destacado=True,
                orden=2,
                activo=True
            ),
            Proyecto(
                titulo_es="API REST de E-commerce",
                titulo_en="E-commerce REST API",
                titulo_it="API REST E-commerce",
                titulo_ca="API REST de Comerç Electrònic",
                descripcion_es="API REST completa para un sistema de e-commerce con gestión de productos, usuarios y pedidos.",
                descripcion_en="Complete REST API for an e-commerce system with product, user and order management.",
                descripcion_it="API REST completa per un sistema e-commerce con gestione prodotti, utenti e ordini.",
                descripcion_ca="API REST completa per a un sistema de comerç electrònic amb gestió de productes, usuaris i comandes.",
                tecnologias=["Python", "FastAPI", "MongoDB", "JWT", "Docker"],
                url_github="https://github.com/geobest7/ecommerce-api",
                url_demo=None,
                imagen_url=None,
                destacado=False,
                orden=3,
                activo=True
            )
        ]
        
        # CURSOS
        cursos = [
            Curso(
                tipo="curso",
                titulo_es="Python Profesional",
                titulo_en="Professional Python",
                titulo_it="Python Professionale",
                titulo_ca="Python Professional",
                institucion_es="Platzi",
                institucion_en="Platzi",
                institucion_it="Platzi",
                institucion_ca="Platzi",
                fecha_inicio=date(2023, 1, 1),
                fecha_fin=date(2023, 3, 1),
                descripcion_es="Curso avanzado de Python con enfoque en programación orientada a objetos, patrones de diseño y buenas prácticas.",
                descripcion_en="Advanced Python course focused on object-oriented programming, design patterns and best practices.",
                descripcion_it="Corso avanzato di Python con focus su programmazione orientata agli oggetti, design pattern e best practices.",
                descripcion_ca="Curs avançat de Python amb enfocament en programació orientada a objectes, patrons de disseny i bones pràctiques.",
                certificado_url=None,
                orden=1,
                activo=True
            ),
            Curso(
                tipo="curso",
                titulo_es="FastAPI: Desarrollo de APIs",
                titulo_en="FastAPI: API Development",
                titulo_it="FastAPI: Sviluppo di API",
                titulo_ca="FastAPI: Desenvolupament d'APIs",
                institucion_es="Udemy",
                institucion_en="Udemy",
                institucion_it="Udemy",
                institucion_ca="Udemy",
                fecha_inicio=date(2024, 1, 1),
                fecha_fin=date(2024, 2, 1),
                descripcion_es="Desarrollo de APIs REST modernas con FastAPI, incluyendo autenticación, validación y documentación automática.",
                descripcion_en="Modern REST API development with FastAPI, including authentication, validation and automatic documentation.",
                descripcion_it="Sviluppo di API REST moderne con FastAPI, inclusa autenticazione, validazione e documentazione automatica.",
                descripcion_ca="Desenvolupament d'APIs REST modernes amb FastAPI, incloent autenticació, validació i documentació automàtica.",
                certificado_url=None,
                orden=2,
                activo=True
            ),
            Curso(
                tipo="curso",
                titulo_es="Git y GitHub",
                titulo_en="Git and GitHub",
                titulo_it="Git e GitHub",
                titulo_ca="Git i GitHub",
                institucion_es="Platzi",
                institucion_en="Platzi",
                institucion_it="Platzi",
                institucion_ca="Platzi",
                fecha_inicio=date(2023, 6, 1),
                fecha_fin=date(2023, 7, 1),
                descripcion_es="Control de versiones con Git y colaboración en GitHub.",
                descripcion_en="Version control with Git and collaboration on GitHub.",
                descripcion_it="Controllo versioni con Git e collaborazione su GitHub.",
                descripcion_ca="Control de versions amb Git i col·laboració a GitHub.",
                certificado_url=None,
                orden=3,
                activo=True
            ),
            Curso(
                tipo="diploma",
                titulo_es="Diploma Técnico Superior",
                titulo_en="Higher Technical Diploma",
                titulo_it="Diploma Tecnico Superiore",
                titulo_ca="Diploma Tècnic Superior",
                institucion_es="Instituto Técnico de Italia",
                institucion_en="Technical Institute of Italy",
                institucion_it="Istituto Tecnico d'Italia",
                institucion_ca="Institut Tècnic d'Itàlia",
                fecha_inicio=date(2020, 9, 1),
                fecha_fin=date(2023, 6, 1),
                descripcion_es="Formación técnica superior en desarrollo de aplicaciones informáticas.",
                descripcion_en="Higher technical training in computer application development.",
                descripcion_it="Formazione tecnica superiore nello sviluppo di applicazioni informatiche.",
                descripcion_ca="Formació tècnica superior en desenvolupament d'aplicacions informàtiques.",
                certificado_url=None,
                orden=0,
                activo=True
            )
        ]
        
        # EXPERIENCIAS
        experiencias = [
            Experiencia(
                tipo="practica",
                empresa="Tech Solutions S.L.",
                cargo_es="Prácticas en Desarrollo Backend",
                cargo_en="Backend Development Internship",
                cargo_it="Stage in Sviluppo Backend",
                cargo_ca="Pràctiques en Desenvolupament Backend",
                fecha_inicio=date(2024, 1, 1),
                fecha_fin=None,
                actual=True,
                descripcion_es="Desarrollo de APIs REST con FastAPI y gestión de bases de datos PostgreSQL. Implementación de sistemas de autenticación y optimización de consultas.",
                descripcion_en="Development of REST APIs with FastAPI and PostgreSQL database management. Implementation of authentication systems and query optimization.",
                descripcion_it="Sviluppo di API REST con FastAPI e gestione di database PostgreSQL. Implementazione di sistemi di autenticazione e ottimizzazione delle query.",
                descripcion_ca="Desenvolupament d'APIs REST amb FastAPI i gestió de bases de dades PostgreSQL. Implementació de sistemes d'autenticació i optimització de consultes.",
                tecnologias=["Python", "FastAPI", "PostgreSQL", "Docker", "Git"],
                orden=1,
                activo=True,
                mostrar_en_web=True
            )
        ]
        
        # Insertar datos
        db.add_all(proyectos)
        db.add_all(cursos)
        db.add_all(experiencias)
        
        db.commit()
        
        print("✅ Base de datos poblada exitosamente!")
        print(f"   - {len(proyectos)} proyectos creados")
        print(f"   - {len(cursos)} cursos creados")
        print(f"   - {len(experiencias)} experiencias creadas")
        
    except Exception as e:
        print(f"❌ Error al poblar la base de datos: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()