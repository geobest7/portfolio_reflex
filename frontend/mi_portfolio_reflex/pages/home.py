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
            rx.box(
                rx.image(
                    src="/foto_perfil.png",
                    width="100%",
                    height="100%",
                    border_radius="50%",
                    object_fit="cover",
                ),
                width="180px",
                height="180px",
                border_radius="50%",
                padding="3px",
                background="linear-gradient(135deg, #333 0%, #666 50%, #333 100%)",
                box_shadow="0 0 30px rgba(255,255,255,0.08)",
                margin_bottom="1em",
                class_name="portada-foto",
            ),
            rx.heading(
                State.hero_titulo,
                size="9",
                font_weight="700",
                letter_spacing="-0.02em",
                color="white",
                class_name="portada-titulo",
            ),
            rx.text(
                State.hero_subtitulo,
                size="5",
                font_weight="300",
                letter_spacing="0.05em",
                color="#999",
                class_name="portada-subtitulo",
            ),
            padding="4em 2em",
            padding_top="7em",
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
