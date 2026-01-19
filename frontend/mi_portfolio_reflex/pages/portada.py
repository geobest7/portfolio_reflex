import reflex as rx
from ..components.selectors import selector_idioma_portada


def portada() -> rx.Component:
    """Página de portada - Solo selector de idioma"""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Alessandro Febbrai", size="9", color="white"),
                rx.text("Select language / Selecciona idioma / Seleziona lingua / Selecciona l'idioma", color="#808080", size="3", text_align="center"),
                selector_idioma_portada(),
                spacing="6",
            ),
        ),
        bg="#000000",
        color="white",
        min_height="100vh",
    )
