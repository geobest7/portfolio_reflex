import reflex as rx
from ..components.selectors import selector_idioma_portada



def portada() -> rx.Component:
    """Página de portada - Solo selector de idioma"""
    return rx.box(
        rx.script(src="/tracking.js"),
        rx.center(
            rx.vstack(
                rx.heading(
                    "PORTFOLIO",
                    size="9",
                    font_weight="800",
                    letter_spacing="0.05em",
                    margin_bottom="0.3em",
                    background="linear-gradient(135deg, #FFFFFF 0%, #999999 100%)",
                    background_clip="text",
                    color="transparent",
                    style={
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                    },
                ),
                rx.text(
                    "by Alessandro Febbrai",
                    size="4",
                    font_weight="400",
                    letter_spacing="0.02em",
                    margin_bottom="2em",
                    background="linear-gradient(135deg, #CCCCCC 0%, #666666 100%)",
                    background_clip="text",
                    color="transparent",
                    style={
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                    },
                ),
                rx.text(
                    "Select language / Selecciona idioma / Seleziona lingua / Selecciona l'idioma",
                    color="#999999",
                    size="3",
                    text_align="center",
                    margin_bottom="1.5em",
                    line_height="1.6",
                ),
                selector_idioma_portada(),
                spacing="4",
                align="center",
                max_width="600px",
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
