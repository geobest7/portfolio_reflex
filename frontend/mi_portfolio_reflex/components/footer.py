import reflex as rx
from ..states import State


def footer() -> rx.Component:
    """Footer con copyright y links sociales"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.icon("github", size=24),
                    href="https://github.com/geobest7",
                    color="white",
                    _hover={"color": "#808080"},
                    is_external=True,
                ),
                rx.link(
                    rx.icon("linkedin", size=24),
                    href="https://linkedin.com/in/alessandro-febbrai",
                    color="white",
                    _hover={"color": "#808080"},
                    is_external=True,
                ),
                rx.link(
                    rx.icon("mail", size=24),
                    href="mailto:tu-email@ejemplo.com",
                    color="white",
                    _hover={"color": "#808080"},
                ),
                spacing="6",
                class_name="footer-social"
            ),
            rx.text(
                f"© 2026 Alessandro Febbrai. {State.footer_derechos}",
                color="#808080",
                size="2",
            ),
            spacing="4",
            align="center",
            padding="2em",
        ),
        bg="#000000",
        border_top="1px solid #333333",
        width="100%",
    )
