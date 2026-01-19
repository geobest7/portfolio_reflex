import reflex as rx
from ..states import State
from ..components import navbar, footer
from ..sections import (
    seccion_sobre_mi,
    seccion_experiencia,
    seccion_formacion,
    seccion_proyectos,
    seccion_github_repos,
    seccion_contacto
)


def home() -> rx.Component:
    """Página Home - Contenido principal del portfolio"""
    return rx.box(
        navbar(),
        rx.vstack(
            rx.image(
                src="/foto_perfil.png",
                width="150px",
                height="150px",
                border_radius="50%",
                margin_bottom="1em",
            ),
            rx.heading(State.hero_titulo, size="9"),
            rx.text(State.hero_subtitulo, size="5"),
            rx.text(State.hero_descripcion),
            padding="4em 2em",
            padding_top="6em",
            spacing="4",
            align="center",
            text_align="center",
            id="inicio"
        ),
        seccion_sobre_mi(),
        seccion_experiencia(),
        seccion_formacion(),
        seccion_proyectos(),
        seccion_github_repos(),
        seccion_contacto(),
        footer(),
        bg="#000000",
        color="white",
        min_height="100vh",
        on_mount=State.cargar_datos_iniciales,
    )
