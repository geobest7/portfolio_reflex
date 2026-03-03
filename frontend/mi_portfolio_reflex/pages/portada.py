import reflex as rx
from ..states import State


def _lang_button(codigo: str, label: str) -> rx.Component:
    """Botón de idioma sencillo B/N para la portada"""
    return rx.button(
        label,
        on_click=[State.cambiar_idioma(codigo), rx.redirect("/home")],
        bg=rx.cond(State.idioma == codigo, "white", "transparent"),
        color=rx.cond(State.idioma == codigo, "#000", "#999"),
        border=rx.cond(State.idioma == codigo, "1px solid white", "1px solid rgba(255,255,255,0.15)"),
        border_radius="8px",
        min_width="48px",
        height="40px",
        font_size="14px",
        font_weight="600",
        letter_spacing="0.05em",
        cursor="pointer",
        class_name="portada-lang-btn",
        _hover={"color": "white", "border_color": "rgba(255,255,255,0.5)"},
    )


def portada() -> rx.Component:
    """Página de portada - Presentación elegante con selector de idioma"""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.image(
                    src="/foto_perfil.png",
                    alt="Alessandro Febbrai - Python Developer",
                    width="140px",
                    height="140px",
                    border_radius="50%",
                    border="3px solid rgba(255,255,255,0.15)",
                    object_fit="cover",
                    class_name="portada-foto",
                ),
                rx.heading(
                    "Alessandro Febbrai",
                    size="8",
                    font_weight="700",
                    letter_spacing="-0.02em",
                    color="white",
                    text_align="center",
                    class_name="portada-titulo",
                ),
                rx.text(
                    "Python Developer",
                    size="5",
                    font_weight="300",
                    letter_spacing="0.15em",
                    color="#888",
                    text_align="center",
                    class_name="portada-rol",
                    style={"text-transform": "uppercase"},
                ),
                rx.box(
                    width="40px",
                    height="1px",
                    bg="rgba(255,255,255,0.2)",
                    margin_y="0.5em",
                    class_name="portada-divider",
                ),
                rx.hstack(
                    _lang_button("es", "ES"),
                    _lang_button("en", "EN"),
                    _lang_button("it", "IT"),
                    _lang_button("ca", "CA"),
                    spacing="3",
                    class_name="portada-idiomas",
                ),
                spacing="4",
                align="center",
                max_width="500px",
                padding="2em",
            ),
        ),
        bg="#000000",
        color="white",
        min_height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
    )
