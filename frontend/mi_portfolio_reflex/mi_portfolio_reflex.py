import reflex as rx
from .state import State


def selector_idioma() -> rx.Component:
    """Componente con 4 botones para cambiar idioma"""
    return rx.hstack(
        rx.button(
            "ES",
            on_click=State.cambiar_idioma("es"),
            bg=rx.cond(State.idioma == "es", "white", "gray"),  # ← CAMBIAR
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "EN",
            on_click=State.cambiar_idioma("en"),
            bg=rx.cond(State.idioma == "en", "white", "gray"),  # ← CAMBIAR
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "IT",
            on_click=State.cambiar_idioma("it"),
            bg=rx.cond(State.idioma == "it", "white", "gray"),  # ← CAMBIAR
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "CA",
            on_click=State.cambiar_idioma("ca"),
            bg=rx.cond(State.idioma == "ca", "white", "gray"),  # ← CAMBIAR
            color="black",
            padding="0.5em",
        ),
        spacing="4",
        padding="4",
    )


def index() -> rx.Component:
    return rx.box(
        selector_idioma(),
        rx.heading(State.hero_titulo, size="9"),
        rx.text(State.hero_subtitulo, size="5"),
        rx.text(State.hero_descripcion),
        rx.hstack(
            rx.button(State.btn_proyectos, bg="#1a1a1a", color="white"),
            rx.button(State.btn_cv, bg="#1a1a1a", color="white"),
            spacing="4",
        ),
        padding="2em",
    )


app = rx.App()
app.add_page(index)