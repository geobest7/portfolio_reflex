import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_repo_github


def seccion_github_repos() -> rx.Component:
    """Sección de repositorios de GitHub con datos dinámicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.github_titulo, size="8", color="white"),
            rx.text(
                State.github_subtitulo,
                color="#CCCCCC",
                size="4",
                text_align="center",
                max_width="600px",
            ),
            
            # Skeleton loaders mientras carga
            rx.cond(
                State.cargando_repos,
                rx.vstack(
                    skeleton_repo_github(),
                    skeleton_repo_github(),
                    skeleton_repo_github(),
                    spacing="3",
                    width="100%",
                    max_width="900px",
                ),
            ),
            
            # Mensaje de error
            rx.cond(
                State.error_repos != "",
                rx.text(State.error_repos, color="red"),
            ),
            
            # Lista de repos
            rx.vstack(
                rx.foreach(
                    State.repos_github,
                    lambda repo: rx.box(
                        rx.vstack(
                            # Nombre del repo
                            rx.heading(
                                repo.name,
                                size="5",
                                color="white",
                            ),
                            # Descripción
                            rx.cond(
                                repo.description != "",
                                rx.text(
                                    repo.description,
                                    color="#CCCCCC",
                                    size="2",
                                ),
                            ),
                            # Stats: lenguaje, stars, forks
                            rx.hstack(
                                # Lenguaje
                                rx.cond(
                                    repo.language != "",
                                    rx.hstack(
                                        rx.icon("code", size=16, color="#00CED1"),
                                        rx.text(repo.language, color="#CCCCCC", size="1"),
                                        spacing="1",
                                    ),
                                ),
                                # Stars
                                rx.hstack(
                                    rx.icon("star", size=16, color="#FFD700"),
                                    rx.text(repo.stargazers_count, color="#CCCCCC", size="1"),
                                    spacing="1",
                                ),
                                # Forks
                                rx.hstack(
                                    rx.icon("git-fork", size=16, color="#CCCCCC"),
                                    rx.text(repo.forks_count, color="#CCCCCC", size="1"),
                                    spacing="1",
                                ),
                                spacing="4",
                                wrap="wrap",
                            ),
                            # Topics/Tags
                            rx.cond(
                                repo.topics.length() > 0,
                                rx.hstack(
                                    rx.foreach(
                                        repo.topics,
                                        lambda topic: rx.badge(
                                            topic,
                                            variant="outline",
                                            color_scheme="blue",
                                            size="1",
                                        ),
                                    ),
                                    wrap="wrap",
                                    spacing="2",
                                ),
                            ),
                            # Link al repo
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("github", size=16),
                                        rx.text(State.github_ver_repo),
                                        spacing="2",
                                    ),
                                    variant="outline",
                                    size="2",
                                ),
                                href=repo.html_url,
                                is_external=True,
                            ),
                            spacing="3",
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
                max_width="900px",
            ),
            
            spacing="5",
            align_items="center",
            width="100%",
        ),
        id="github",
        padding="4em 2em",
        background_color="#0A0A0A",
    )
