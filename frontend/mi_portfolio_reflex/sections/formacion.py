import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_curso


def _titulo_curso(curso) -> rx.Component:
    return rx.cond(
        State.idioma == "es", curso.titulo_es,
        rx.cond(
            State.idioma == "en", curso.titulo_en,
            rx.cond(State.idioma == "it", curso.titulo_it, curso.titulo_ca)
        )
    )


def _institucion_curso(curso) -> rx.Component:
    return rx.cond(
        State.idioma == "es", curso.institucion_es,
        rx.cond(
            State.idioma == "en", curso.institucion_en,
            rx.cond(State.idioma == "it", curso.institucion_it, curso.institucion_ca)
        )
    )


def _descripcion_curso(curso) -> rx.Component:
    return rx.cond(
        State.idioma == "es", curso.descripcion_es,
        rx.cond(
            State.idioma == "en", curso.descripcion_en,
            rx.cond(State.idioma == "it", curso.descripcion_it, curso.descripcion_ca)
        )
    )


def _curso_card(curso) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    curso.tipo.upper(),
                    color=rx.cond(curso.tipo == "diploma", "#FFD700", "#00CED1"),
                    font_weight="bold",
                    size="2",
                ),
                rx.text(
                    _titulo_curso(curso),
                    color="white",
                    font_weight="bold",
                    size="4",
                ),
                spacing="3",
                align_items="center",
            ),
            rx.text(
                _institucion_curso(curso),
                color="#CCCCCC",
                size="2",
            ),
            rx.text(
                rx.cond(
                    curso.fecha_fin != "",
                    f"{curso.fecha_inicio} - {curso.fecha_fin}",
                    f"{curso.fecha_inicio}"
                ),
                color="#999999",
                size="1",
            ),
            rx.cond(
                curso.descripcion_es != "",
                rx.box(
                    rx.text(
                        _descripcion_curso(curso),
                        color="#AAAAAA",
                        size="2",
                        line_height="1.6",
                    ),
                    padding="0.8em 0",
                    width="100%",
                ),
            ),
            rx.hstack(
                rx.cond(
                    curso.certificado_url != "",
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("award", size=14),
                                rx.text(State.ver_certificado),
                                spacing="2",
                                align="center",
                            ),
                            size="1",
                            variant="outline",
                        ),
                        href=curso.certificado_url,
                        is_external=True,
                    ),
                ),
                rx.cond(
                    curso.diploma_pdf != "",
                    rx.button(
                        rx.hstack(
                            rx.icon("scroll-text", size=14),
                            rx.text(State.ver_diploma),
                            spacing="2",
                            align="center",
                        ),
                        size="1",
                        variant="solid",
                        color_scheme="yellow",
                        on_click=State.abrir_diploma(curso.diploma_pdf),
                    ),
                ),
                spacing="3",
            ),
            spacing="2",
            align_items="start",
        ),
        padding="1.5em",
        border_radius="10px",
        border="1px solid rgba(255,255,255,0.08)",
        background_color="rgba(255,255,255,0.02)",
        width="100%",
        _hover={"border_color": "rgba(255,255,255,0.15)", "background_color": "rgba(255,255,255,0.04)"},
        transition="all 0.3s ease",
        class_name="fade-in-up",
    )


def seccion_formacion() -> rx.Component:
    """Seccion Formacion con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.formacion_titulo, size="8", color="white", text_align="center", width="100%"),
            
            rx.cond(
                State.cargando_cursos,
                rx.vstack(
                    skeleton_curso(),
                    skeleton_curso(),
                    skeleton_curso(),
                    spacing="3",
                    width="100%",
                    max_width="800px",
                ),
            ),
            
            rx.cond(
                State.error_cursos != "",
                rx.text(State.error_cursos, color="red"),
            ),
            
            rx.vstack(
                rx.foreach(State.cursos, _curso_card),
                spacing="3",
                width="100%",
                max_width="800px",
            ),
            
            spacing="5",
            align_items="center",
            width="100%",
        ),
        id="formacion",
        padding="4em 2em",
        background_color="#000000",
    )
