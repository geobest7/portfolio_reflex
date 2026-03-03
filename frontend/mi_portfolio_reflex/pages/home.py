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
                    alt="Alessandro Febbrai - Python Developer",
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
            rx.box(
                rx.text(
                    " ",
                    id="typing-text",
                    class_name="portada-subtitulo",
                ),
                rx.el.input(
                    type="hidden",
                    id="current-lang",
                    value=State.idioma,
                ),
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
        # Scroll-to-top button (visible via JS when scrolled > 400px)
        rx.el.button(
            rx.icon("chevron-up", size=24, color="white"),
            id="scroll-top-btn",
            on_click=rx.call_script("window.scrollTo({top:0,behavior:'smooth'})"),
            style={
                "position": "fixed",
                "bottom": "2rem",
                "right": "2rem",
                "width": "48px",
                "height": "48px",
                "border_radius": "50%",
                "background": "rgba(255,255,255,0.1)",
                "border": "1px solid rgba(255,255,255,0.2)",
                "backdrop_filter": "blur(8px)",
                "cursor": "pointer",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "opacity": "0",
                "pointer_events": "none",
                "transition": "opacity 0.3s ease, transform 0.3s ease",
                "z_index": "900",
            },
        ),
        bg="#000000",
        color="white",
        min_height="100vh",
        on_mount=State.cargar_datos_iniciales,
    )
