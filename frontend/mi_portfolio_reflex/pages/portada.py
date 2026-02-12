import reflex as rx
from ..components.selectors import selector_idioma_portada

_TRACKING_SCRIPT = """
(function() {
    if (window._tracked) return;
    window._tracked = true;
    try {
        var api = window.location.hostname === 'localhost'
            ? 'http://localhost:8001'
            : 'https://portfolio-reflex-pwdv.onrender.com';
        fetch(api + '/api/analytics/track', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                pagina: window.location.pathname,
                referrer: document.referrer || '',
                user_agent: navigator.userAgent || '',
                screen_width: window.screen.width,
                screen_height: window.screen.height,
                idioma: navigator.language || '',
                plataforma: navigator.platform || ''
            })
        });
    } catch(e) {}
})();
"""


def portada() -> rx.Component:
    """Página de portada - Solo selector de idioma"""
    return rx.box(
        rx.script(_TRACKING_SCRIPT),
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
