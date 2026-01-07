import reflex as rx
from .state import State


def selector_idioma_portada() -> rx.Component:
    """Selector de idioma para la portada con redirección"""
    return rx.hstack(
        rx.button(
            "ES",
            on_click=[State.cambiar_idioma("es"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "es", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "EN",
            on_click=[State.cambiar_idioma("en"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "en", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "IT",
            on_click=[State.cambiar_idioma("it"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "it", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "CA",
            on_click=[State.cambiar_idioma("ca"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "ca", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        spacing="4",
    )


def selector_idioma() -> rx.Component:
    """Selector de idioma para navbar (sin redirección)"""
    return rx.hstack(
        rx.button(
            "ES",
            on_click=State.cambiar_idioma("es"),
            bg=rx.cond(State.idioma == "es", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "EN",
            on_click=State.cambiar_idioma("en"),
            bg=rx.cond(State.idioma == "en", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "IT",
            on_click=State.cambiar_idioma("it"),
            bg=rx.cond(State.idioma == "it", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "CA",
            on_click=State.cambiar_idioma("ca"),
            bg=rx.cond(State.idioma == "ca", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        spacing="4",
        padding="4",
    )


def navbar() -> rx.Component:
    """Barra de navegación con links y selector de idioma"""
    return rx.box(
        rx.hstack(
            rx.heading("AF", size="7", color="white"),
            rx.spacer(),
            rx.hstack(
                rx.link(State.nav_inicio, href="#inicio", color="white"),
                rx.link(State.nav_sobre_mi, href="#sobre-mi", color="white"),
                rx.link(State.nav_proyectos, href="#proyectos", color="white"),
                rx.link(State.nav_contacto, href="#contacto", color="white"),
                spacing="6",
            ),
            rx.spacer(),
            selector_idioma(),
            width="100%",
            align="center",
        ),
        bg="#000000",
        padding="1em 2em",
        width="100%",
    )


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


def home() -> rx.Component:
    """Página home - Con navbar y contenido"""
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.hero_titulo, size="9"),
            rx.text(State.hero_subtitulo, size="5"),
            rx.text(State.hero_descripcion),
            rx.hstack(
                rx.button(State.btn_proyectos, bg="#1a1a1a", color="white"),
                rx.button(State.btn_cv, bg="#1a1a1a", color="white"),
                spacing="4",
            ),
            padding="4em 2em",
            spacing="4",
        ),
        bg="#000000",
        color="white",
        min_height="100vh",
    )


app = rx.App()
app.add_page(portada, route="/")
app.add_page(home, route="/home")