import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_curso


def seccion_formacion() -> rx.Component:
    """Seccion Formacion con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.formacion_titulo, size="8", color="white"),
            
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
                rx.foreach(
                    State.cursos,
                    lambda curso: rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    curso.tipo.upper(),
                                    color=rx.cond(
                                        curso.tipo == "diploma",
                                        "#FFD700",
                                        "#00CED1"
                                    ),
                                    font_weight="bold",
                                    size="2",
                                ),
                                rx.text(
                                    rx.cond(
                                        State.idioma == "es",
                                        curso.titulo_es,
                                        rx.cond(
                                            State.idioma == "en",
                                            curso.titulo_en,
                                            rx.cond(
                                                State.idioma == "it",
                                                curso.titulo_it,
                                                curso.titulo_ca
                                            )
                                        )
                                    ),
                                    color="white",
                                    font_weight="bold",
                                    size="4",
                                ),
                                spacing="3",
                                align_items="center",
                            ),
                            rx.text(
                                rx.cond(
                                    State.idioma == "es", curso.institucion_es,
                                    rx.cond(
                                        State.idioma == "en", curso.institucion_en,
                                        rx.cond(
                                            State.idioma == "it", curso.institucion_it,
                                            curso.institucion_ca
                                        )
                                    )
                                ),
                                color="#CCCCCC",
                                size="2",
                            ),
                            rx.text(
                                rx.cond(
                                    curso.fecha_fin != "",
                                    f"{curso.fecha_inicio} - {curso.fecha_fin}",
                                    f"{curso.fecha_inicio} - Actualidad"
                                ),
                                color="#999999",
                                size="1",
                            ),
                            rx.cond(
                                curso.certificado_url != "",
                                rx.link(
                                    rx.button("Ver certificado", size="1", variant="outline"),
                                    href=curso.certificado_url,
                                    is_external=True,
                                ),
                            ),
                            rx.cond(
                                curso.diploma_pdf != "",
                                rx.link(
                                    rx.button("Ver Diploma", size="1", variant="solid", color_scheme="cyan"),
                                    href=curso.diploma_pdf,
                                    is_external=True,
                                ),
                            ),
                            spacing="2",
                            align_items="start",
                        ),
                        padding="1.5em",
                        border_radius="8px",
                        border="1px solid #333333",
                        background_color="#0A0A0A",
                        width="100%",
                        class_name="fade-in-up",
                    )
                ),
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
