import reflex as rx
from ..states import State


def seccion_sobre_mi() -> rx.Component:
    """Sección Sobre mí"""
    return rx.box(
        rx.vstack(
            rx.heading(State.sobre_mi_titulo, size="8", color="white"),
            rx.text(
                State.sobre_mi_descripcion,
                color="#cccccc",
                size="4",
                line_height="1.8",
                max_width="800px",
            ),
            # Habilidades técnicas (ahora al final)
            rx.heading(State.habilidades_titulo, size="6", color="white", margin_top="2em"),
            rx.hstack(
                rx.badge("Python", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("Reflex", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("FastAPI", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("JavaScript", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("Git", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                spacing="3",
                wrap="wrap",
            ),
            
            spacing="4",
            align="center",
            text_align="center",
        ),
        padding="6em 2em",
        id="sobre-mi",
    )
