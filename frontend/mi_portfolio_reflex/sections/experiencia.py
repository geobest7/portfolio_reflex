import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_experiencia


def _cargo_exp(exp) -> rx.Component:
    return rx.cond(
        State.idioma == "es", exp.cargo_es,
        rx.cond(
            State.idioma == "en", exp.cargo_en,
            rx.cond(State.idioma == "it", exp.cargo_it, exp.cargo_ca)
        )
    )


def _descripcion_exp(exp) -> rx.Component:
    return rx.cond(
        State.idioma == "es", exp.descripcion_es,
        rx.cond(
            State.idioma == "en", exp.descripcion_en,
            rx.cond(State.idioma == "it", exp.descripcion_it, exp.descripcion_ca)
        )
    )


def _exp_card(exp) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    exp.tipo.upper(),
                    color=rx.cond(exp.tipo == "practica", "#00CED1", "#4CAF50"),
                    font_weight="bold",
                    size="2",
                ),
                spacing="3",
                align_items="center",
            ),
            rx.hstack(
                rx.icon("briefcase", size=24, color=rx.cond(exp.tipo == "practica", "#00CED1", "#4CAF50")),
                rx.vstack(
                    rx.text(_cargo_exp(exp), size="4", weight="bold", color=rx.cond(exp.tipo == "practica", "#00CED1", "#4CAF50")),
                    rx.text(exp.empresa, size="3", color="#CCCCCC"),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="start",
            ),
            rx.hstack(
                rx.icon("calendar", size=20, color="#CCCCCC"),
                rx.text(exp.fecha_inicio + " - " + rx.cond(exp.actual, "Actualidad", exp.fecha_fin), size="3", color="#CCCCCC"),
                spacing="2",
            ),
            # Descripcion
            rx.cond(
                exp.descripcion_es != "",
                rx.box(
                    rx.text(
                        _descripcion_exp(exp),
                        color="#AAAAAA",
                        size="2",
                        line_height="1.6",
                    ),
                    padding="0.5em 0",
                    width="100%",
                ),
            ),
            # Tecnologias
            rx.hstack(
                rx.foreach(
                    exp.tecnologias,
                    lambda tech: rx.badge(tech, variant="outline", color_scheme="gray"),
                ),
                wrap="wrap",
                spacing="2",
            ),
            # Imagen
            rx.cond(
                exp.imagen_url != "",
                rx.image(
                    src=exp.imagen_url,
                    width="100%",
                    max_height="300px",
                    object_fit="cover",
                    border_radius="8px",
                    margin_top="0.5em",
                    loading="lazy",
                ),
            ),
            # Video (HTML5 nativo - Cloudinary) con poster auto-generado
            rx.cond(
                exp.video_url != "",
                rx.box(
                    rx.el.video(
                        rx.el.source(src=exp.video_url, type="video/mp4"),
                        controls=True,
                        preload="none",
                        poster=exp.video_url.replace("/video/upload/", "/video/upload/so_0,w_600,q_auto/").replace(".mp4", ".jpg").replace(".webm", ".jpg").replace(".mov", ".jpg"),
                        width="100%",
                        style={"border_radius": "8px", "max_height": "400px", "background": "#111"},
                    ),
                    width="100%",
                    margin_top="0.5em",
                ),
            ),
            # Documento PDF
            rx.cond(
                exp.documento_url != "",
                rx.button(
                    rx.hstack(
                        rx.icon("file-text", size=14),
                        rx.text(State.ver_diploma),
                        spacing="2",
                        align="center",
                    ),
                    size="1",
                    variant="solid",
                    color_scheme="yellow",
                    on_click=State.abrir_diploma(exp.documento_url),
                ),
            ),
            spacing="4",
            align="start",
        ),
        padding="1.5em",
        border_radius="10px",
        border="1px solid rgba(255,255,255,0.08)",
        bg="rgba(255,255,255,0.02)",
        width="100%",
        _hover={"border_color": "rgba(255,255,255,0.15)", "bg": "rgba(255,255,255,0.04)"},
        transition="all 0.3s ease",
        class_name="fade-in-up",
    )


def seccion_experiencia() -> rx.Component:
    """Seccion Experiencia con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.experiencia_titulo, size="8", color="white", text_align="center", width="100%"),
            rx.cond(
                State.cargando_experiencias,
                rx.vstack(
                    skeleton_experiencia(),
                    spacing="3",
                    width="100%",
                    max_width="800px",
                ),
            ),
            rx.cond(
                State.error_experiencias != "",
                rx.text(State.error_experiencias, color="red"),
            ),
            rx.vstack(
                rx.foreach(State.experiencias, _exp_card),
                spacing="3",
                width="100%",
                max_width="800px",
            ),
            spacing="5",
            align_items="center",
            width="100%",
        ),
        id="experiencia",
        padding="4em 2em",
        background_color="#000000",
    )
