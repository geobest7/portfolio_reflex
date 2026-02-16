import reflex as rx
from ..states import State
from ..components import navbar, footer
from ..sections import (
    seccion_sobre_mi,
    seccion_experiencia,
    seccion_formacion,
    seccion_proyectos,
    seccion_github_repos,
    seccion_contacto
)


_TRACKING_JS = """
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


def home() -> rx.Component:
    """Página Home - Contenido principal del portfolio"""
    return rx.box(
        rx.el.script(_TRACKING_JS),
        navbar(),
        rx.vstack(
            rx.image(
                src="/foto_perfil.png",
                width="150px",
                height="150px",
                border_radius="50%",
                border="4px solid #EEEEEE",
                box_shadow="0 8px 32px rgba(255, 255, 255, 0.1)",
                margin_bottom="1em",
            ),
            rx.heading(
                State.hero_titulo,
                size="9",
                background="linear-gradient(135deg, #FFFFFF 0%, #999999 100%)",
                background_clip="text",
                color="transparent",
                style={
                    "-webkit-background-clip": "text",
                    "-webkit-text-fill-color": "transparent",
                },
            ),
            rx.text(
                State.hero_subtitulo,
                size="5",
                background="linear-gradient(135deg, #CCCCCC 0%, #666666 100%)",
                background_clip="text",
                color="transparent",
                style={
                    "-webkit-background-clip": "text",
                    "-webkit-text-fill-color": "transparent",
                },
            ),
            padding="4em 2em",
            padding_top="6em",
            spacing="4",
            align="center",
            text_align="center",
            id="inicio"
        ),
        seccion_sobre_mi(),
        seccion_experiencia(),
        seccion_formacion(),
        seccion_proyectos(),
        seccion_github_repos(),
        seccion_contacto(),
        footer(),
        bg="#000000",
        color="white",
        min_height="100vh",
        on_mount=State.cargar_datos_iniciales,
    )
