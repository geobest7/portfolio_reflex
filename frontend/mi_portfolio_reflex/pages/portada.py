import reflex as rx
from ..states import State


def _lang_button(codigo: str, flag: str, label: str) -> rx.Component:
    """Botón de idioma con bandera para la portada"""
    return rx.button(
        rx.vstack(
            rx.text(flag, font_size="24px", line_height="1"),
            rx.text(label, font_size="12px", font_weight="600", color=rx.cond(State.idioma == codigo, "#000", "#ccc")),
            spacing="1",
            align="center",
        ),
        on_click=[State.cambiar_idioma(codigo), rx.redirect("/home")],
        bg=rx.cond(State.idioma == codigo, "rgba(255,255,255,0.95)", "rgba(255,255,255,0.06)"),
        border=rx.cond(State.idioma == codigo, "1px solid rgba(255,255,255,0.9)", "1px solid rgba(255,255,255,0.12)"),
        border_radius="12px",
        width="72px",
        height="68px",
        cursor="pointer",
        class_name="portada-lang-btn",
        _hover={"bg": rx.cond(State.idioma == codigo, "rgba(255,255,255,1)", "rgba(255,255,255,0.12)")},
    )


def portada() -> rx.Component:
    """Página de portada - Presentación elegante con selector de idioma"""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.image(
                    src="/foto_perfil.png",
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
                    _lang_button("es", "🇪🇸", "ES"),
                    _lang_button("en", "🇬🇧", "EN"),
                    _lang_button("it", "🇮🇹", "IT"),
                    _lang_button("ca", "🏳️", "CA"),
                    spacing="3",
                    class_name="portada-idiomas",
                ),
                rx.box(
                    rx.icon("chevron-down", size=20, color="rgba(255,255,255,0.3)"),
                    class_name="portada-scroll-hint",
                    margin_top="2em",
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
