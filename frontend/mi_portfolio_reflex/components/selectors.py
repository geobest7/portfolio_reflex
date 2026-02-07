import reflex as rx
from ..states import State


def _boton_idioma_portada(codigo: str, label: str) -> rx.Component:
    """Botón de idioma reutilizable para la portada"""
    return rx.button(
        label,
        on_click=[State.cambiar_idioma(codigo), rx.redirect("/home")],
        bg=rx.cond(State.idioma == codigo, "#EEEEEE", "#1a1a1a"),
        color=rx.cond(State.idioma == codigo, "#000000", "#CCCCCC"),
        min_width="55px",
        height="42px",
        font_size="15px",
        font_weight="600",
        border=rx.cond(State.idioma == codigo, "2px solid #EEEEEE", "2px solid #333"),
        border_radius="8px",
        cursor="pointer",
        _hover={"bg": rx.cond(State.idioma == codigo, "#FFFFFF", "#2a2a2a"), "transform": "scale(1.05)"},
        transition="all 0.2s ease",
        flex_shrink="0",
    )


def selector_idioma_portada() -> rx.Component:
    """Selector de idioma para la portada con redirección"""
    return rx.hstack(
        _boton_idioma_portada("es", "ES"),
        _boton_idioma_portada("en", "EN"),
        _boton_idioma_portada("it", "IT"),
        _boton_idioma_portada("ca", "CA"),
        spacing="3",
        wrap="wrap",
        justify="center",
        width="100%",
        max_width="300px",
    )


def _boton_idioma_navbar(codigo: str, label: str) -> rx.Component:
    """Botón de idioma reutilizable para navbar"""
    return rx.button(
        label,
        on_click=State.cambiar_idioma(codigo),
        bg=rx.cond(State.idioma == codigo, "#EEEEEE", "#1a1a1a"),
        color=rx.cond(State.idioma == codigo, "#000000", "#CCCCCC"),
        min_width="40px",
        height="32px",
        font_size="13px",
        font_weight="600",
        border=rx.cond(State.idioma == codigo, "2px solid #EEEEEE", "2px solid #333"),
        border_radius="6px",
        cursor="pointer",
        _hover={"bg": rx.cond(State.idioma == codigo, "#FFFFFF", "#2a2a2a")},
        transition="all 0.2s ease",
        flex_shrink="0",
    )


def selector_idioma() -> rx.Component:
    """Selector de idioma para navbar (sin redirección)"""
    return rx.hstack(
        _boton_idioma_navbar("es", "ES"),
        _boton_idioma_navbar("en", "EN"),
        _boton_idioma_navbar("it", "IT"),
        _boton_idioma_navbar("ca", "CA"),
        spacing="2",
        wrap="wrap",
        justify="center",
        flex_shrink="0",
    )
