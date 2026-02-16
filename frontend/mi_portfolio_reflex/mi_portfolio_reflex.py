import reflex as rx
from .pages import portada, home, pagina_cv, pagina_login
from .admin import dashboard_admin, admin_proyectos, formulario_proyecto, admin_cursos, formulario_curso, admin_experiencias, formulario_experiencia, admin_analytics
from .states import State


app = rx.App(
    stylesheets=[
        "styles/styles.css",
    ],
)

app.add_page(
    portada,
    route="/",
    title="Alessandro Febbrai | Portfolio",
    description="Portfolio de Alessandro Febbrai - Desarrollador Python Junior. Proyectos, formación y experiencia en desarrollo web.",
    on_load=State.registrar_visita,
    meta=[
        {"property": "og:title", "content": "Alessandro Febbrai | Portfolio"},
        {"property": "og:description", "content": "Portfolio de Alessandro Febbrai - Desarrollador Python Junior"},
        {"property": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary"},
        {"name": "twitter:title", "content": "Alessandro Febbrai | Portfolio"},
        {"name": "twitter:description", "content": "Desarrollador Python Junior - Portfolio profesional"},
        {"name": "keywords", "content": "Alessandro Febbrai, Python, desarrollador, portfolio, FastAPI, Reflex, web developer"},
        {"name": "author", "content": "Alessandro Febbrai"},
        {"name": "robots", "content": "index, follow"},
    ],
)
app.add_page(
    home,
    route="/home",
    title="Alessandro Febbrai | Desarrollador Python",
    description="Sobre mí, proyectos, formación y experiencia profesional de Alessandro Febbrai. Desarrollo web con Python, FastAPI y Reflex.",
    on_load=State.registrar_visita,
    meta=[
        {"property": "og:title", "content": "Alessandro Febbrai | Desarrollador Python"},
        {"property": "og:description", "content": "Proyectos, formación y experiencia en desarrollo web con Python"},
        {"property": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary"},
        {"name": "twitter:title", "content": "Alessandro Febbrai | Desarrollador Python"},
        {"name": "robots", "content": "index, follow"},
    ],
)
app.add_page(
    pagina_cv,
    route="/cv",
    title="CV | Alessandro Febbrai",
    description="Currículum Vitae de Alessandro Febbrai - Desarrollador Python Junior",
    meta=[
        {"name": "robots", "content": "noindex"},
    ],
)
app.add_page(pagina_login, route="/login")
app.add_page(dashboard_admin, route="/admin")
app.add_page(admin_proyectos, route="/admin/proyectos")
app.add_page(formulario_proyecto, route="/admin/proyectos/form")
app.add_page(admin_cursos, route="/admin/cursos")
app.add_page(formulario_curso, route="/admin/cursos/form")
app.add_page(admin_experiencias, route="/admin/experiencias")
app.add_page(formulario_experiencia, route="/admin/experiencias/form")
app.add_page(admin_analytics, route="/admin/analytics")
