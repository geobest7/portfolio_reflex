import reflex as rx
from ..states import State
from ..components import navbar


def pagina_diploma() -> rx.Component:
    """Página Diploma - PDF a pantalla completa con botón de descarga (mismo patrón que CV)"""
    return rx.box(
        navbar(),
        rx.cond(
            State.diploma_url_actual != "",
            rx.box(
                rx.el.iframe(
                    src=State.diploma_url_actual,
                    style={
                        "position": "absolute",
                        "top": "4em",
                        "left": "0",
                        "width": "100%",
                        "height": "calc(100% - 4em)",
                        "border": "none",
                    },
                ),
                rx.link(
                    rx.button(
                        "Descargar diploma",
                        size="2",
                        variant="solid",
                        color_scheme="gray",
                    ),
                    href=State.diploma_url_actual,
                    download=True,
                    is_external=True,
                    style={
                        "position": "fixed",
                        "bottom": "2em",
                        "right": "2em",
                        "z_index": "1000",
                    },
                ),
                width="100%",
                height="100vh",
                position="relative",
            ),
            rx.vstack(
                rx.text(
                    "No se ha seleccionado ningún diploma.",
                    color="#999999",
                    size="4",
                ),
                rx.link(
                    rx.button("Volver", variant="outline", color_scheme="gray"),
                    href="/home#formacion",
                ),
                align="center",
                justify="center",
                height="80vh",
                spacing="4",
            ),
        ),
        bg="#000000",
        width="100%",
        height="100vh",
        position="relative",
    )
