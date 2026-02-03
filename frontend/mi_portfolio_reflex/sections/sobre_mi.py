import reflex as rx
from ..states import State


def seccion_sobre_mi() -> rx.Component:
    """Sección Sobre mí"""
    return rx.box(
        rx.vstack(
            rx.heading(State.sobre_mi_titulo, size="8", color="white"),
            rx.text(
                State.sobre_mi_descripcion,
                color="#cccccc",
                size="4",
                line_height="1.8",
                max_width="800px",
            ),
            # Habilidades técnicas con iconos
            rx.heading(State.habilidades_titulo, size="6", color="white", margin_top="2em"),
            rx.hstack(
                # Python
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
                            width="50px",
                            height="50px",
                        ),
                        rx.text("Python", color="white", font_size="14px", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="1em",
                    border_radius="8px",
                    bg="#1a1a1a",
                    border="2px solid #333",
                    _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
                    transition="all 0.3s ease",
                ),
                # Reflex
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="https://reflex.dev/logo.svg",
                            width="50px",
                            height="50px",
                        ),
                        rx.text("Reflex", color="white", font_size="14px", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="1em",
                    border_radius="8px",
                    bg="#1a1a1a",
                    border="2px solid #333",
                    _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
                    transition="all 0.3s ease",
                ),
                # FastAPI
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg",
                            width="50px",
                            height="50px",
                        ),
                        rx.text("FastAPI", color="white", font_size="14px", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="1em",
                    border_radius="8px",
                    bg="#1a1a1a",
                    border="2px solid #333",
                    _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
                    transition="all 0.3s ease",
                ),
                # JavaScript
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
                            width="50px",
                            height="50px",
                        ),
                        rx.text("JavaScript", color="white", font_size="14px", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="1em",
                    border_radius="8px",
                    bg="#1a1a1a",
                    border="2px solid #333",
                    _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
                    transition="all 0.3s ease",
                ),
                # Git
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
                            width="50px",
                            height="50px",
                        ),
                        rx.text("Git", color="white", font_size="14px", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="1em",
                    border_radius="8px",
                    bg="#1a1a1a",
                    border="2px solid #333",
                    _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
                    transition="all 0.3s ease",
                ),
                spacing="4",
                wrap="wrap",
                justify="center",
            ),
            
            spacing="4",
            align="center",
            text_align="center",
        ),
        padding="6em 2em",
        id="sobre-mi",
    )
