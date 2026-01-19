import reflex as rx
from .pages import portada, home, pagina_cv, pagina_login
from .admin import dashboard_admin, admin_proyectos, formulario_proyecto, admin_cursos, formulario_curso, admin_experiencias, formulario_experiencia


app = rx.App(
    stylesheets=[
        "styles/styles.css",
    ],
)

app.add_page(portada, route="/")
app.add_page(home, route="/home")
app.add_page(pagina_cv, route="/cv")
app.add_page(pagina_login, route="/login")
app.add_page(dashboard_admin, route="/admin")
app.add_page(admin_proyectos, route="/admin/proyectos")
app.add_page(formulario_proyecto, route="/admin/proyectos/form")
app.add_page(admin_cursos, route="/admin/cursos")
app.add_page(formulario_curso, route="/admin/cursos/form")
app.add_page(admin_experiencias, route="/admin/experiencias")
app.add_page(formulario_experiencia, route="/admin/experiencias/form")
