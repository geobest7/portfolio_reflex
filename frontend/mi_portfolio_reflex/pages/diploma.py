import reflex as rx
from ..states import State
from ..components import navbar


def pagina_diploma() -> rx.Component:
    """Página Diploma - PDF viewer integrado como el CV"""
    return rx.box(
        navbar(),
        rx.cond(
            State.diploma_url_actual != "",
            rx.el.iframe(
                src="https://docs.google.com/gview?url=" + State.diploma_url_actual + "&embedded=true",
                style={
                    "position": "absolute",
                    "top": "4em",
                    "left": "0",
                    "width": "100%",
                    "height": "calc(100% - 4em)",
                    "border": "none",
                },
            ),
            rx.center(
                rx.vstack(
                    rx.text("No hay diploma seleccionado", color="white", size="4"),
                    rx.link(
                        rx.button("Volver", variant="outline"),
                        href="/home#formacion",
                    ),
                    align="center",
                    spacing="4",
                ),
                padding_top="6em",
            ),
        ),
        bg="#000000",
        width="100%",
        height="100vh",
        position="relative",
    )
