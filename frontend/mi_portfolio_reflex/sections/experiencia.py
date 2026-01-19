import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_experiencia


def seccion_experiencia() -> rx.Component:
    """Seccion Experiencia con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading("Experiencia", size="8", color="white"),
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
                rx.foreach(
                    State.experiencias,
                    lambda exp: rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("briefcase", size=24, color="white"),
                                rx.vstack(
                                    rx.text(
                                        rx.cond(
                                            State.idioma == "es",
                                            exp.cargo_es,
                                            rx.cond(
                                                State.idioma == "en",
                                                exp.cargo_en,
                                                rx.cond(State.idioma == "it", exp.cargo_it, exp.cargo_ca)
                                            )
                                        ),
                                        size="4",
                                        weight="bold",
                                        color="white",
                                    ),
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
                            rx.hstack(
                                rx.foreach(
                                    exp.tecnologias,
                                    lambda tech: rx.badge(tech, variant="outline", color_scheme="gray"),
                                ),
                                wrap="wrap",
                                spacing="2",
                            ),
                            rx.cond(
                                exp.video_url != "",
                                rx.box(
                                    rx.html('<iframe width="100%" height="315" src="' + exp.video_url + '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'),
                                    width="100%",
                                    margin_top="1em",
                                ),
                            ),
                            spacing="4",
                            align="start",
                        ),
                        padding="1.5em",
                        border_radius="8px",
                        border="1px solid #333333",
                        bg="#0a0a0a",
                        width="100%",
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
        id="experiencia",
        padding="4em 2em",
        background_color="#000000",
    )
