import reflex as rx
from ..components import navbar


def pagina_cv() -> rx.Component:
    """Página CV - PDF a pantalla completa con botón de descarga"""
    return rx.box(
        navbar(),
        # PDF a pantalla completa con position absolute
        rx.html(
            '<iframe src="/CV.pdf" style="position: absolute; top: 4em; left: 0; width: 100%; height: calc(100% - 4em); border: none;"></iframe>',
        ),
        bg="#000000",
        width="100%",
        height="100vh",
        position="relative",
    )
