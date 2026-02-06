import reflex as rx
from ..states import State


TECNOLOGIAS = [
    ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
    ("Jupyter", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg"),
    ("NumPy", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"),
    ("Pandas", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"),
    ("Reflex", "https://reflex.dev/logo.svg"),
    ("Windsurf AI", "https://windsurf.com/favicon.svg"),
    ("FastAPI", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg"),
    ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
    ("GitHub", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"),
    ("VS Code", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"),
    ("Flask", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"),
    ("Django", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"),
    ("PyCharm", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg"),
    ("Anaconda", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg"),
    ("JavaScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"),
    ("Node.js", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"),
    ("Bitbucket", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bitbucket/bitbucket-original.svg"),
    ("Docker", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"),
]


def _tech_card(nombre: str, icon_url: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=icon_url,
                width="50px",
                height="50px",
            ),
            rx.text(nombre, color="white", font_size="14px", font_weight="600"),
            spacing="2",
            align="center",
        ),
        padding="1em",
        border_radius="8px",
        bg="#1a1a1a",
        border="2px solid #333",
        _hover={"border_color": "#00CED1", "transform": "translateY(-5px)"},
        transition="all 0.3s ease",
    )


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
            rx.heading(State.tecnologias_titulo, size="6", color="white", margin_top="2em"),
            rx.hstack(
                *[_tech_card(nombre, url) for nombre, url in TECNOLOGIAS],
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
