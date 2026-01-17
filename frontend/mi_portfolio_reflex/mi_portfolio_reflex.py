import reflex as rx
from .state import State



def selector_idioma_portada() -> rx.Component:
    """Selector de idioma para la portada con redirección"""
    return rx.hstack(
        rx.button(
            "ES",
            on_click=[State.cambiar_idioma("es"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "es", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "EN",
            on_click=[State.cambiar_idioma("en"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "en", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "IT",
            on_click=[State.cambiar_idioma("it"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "it", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "CA",
            on_click=[State.cambiar_idioma("ca"), rx.redirect("/home")],
            bg=rx.cond(State.idioma == "ca", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        spacing="4",
    )


def selector_idioma() -> rx.Component:
    """Selector de idioma para navbar (sin redirección)"""
    return rx.hstack(
        rx.button(
            "ES",
            on_click=State.cambiar_idioma("es"),
            bg=rx.cond(State.idioma == "es", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "EN",
            on_click=State.cambiar_idioma("en"),
            bg=rx.cond(State.idioma == "en", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "IT",
            on_click=State.cambiar_idioma("it"),
            bg=rx.cond(State.idioma == "it", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        rx.button(
            "CA",
            on_click=State.cambiar_idioma("ca"),
            bg=rx.cond(State.idioma == "ca", "white", "gray"),
            color="black",
            padding="0.5em",
        ),
        spacing="4",
        padding="4",
    )


def navbar() -> rx.Component:
    """Barra de navegación con links y selector de idioma"""
    return rx.box(
        rx.hstack(
            rx.image(
                src="/logo.png",
                height="40px",
                alt="Alessandro Febbrai",
            ),
            rx.spacer(),
            # Links desktop (ocultos en móvil)
            rx.hstack(
                rx.link(State.nav_inicio, href="/home#inicio", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_sobre_mi, href="/home#sobre-mi", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_experiencia, href="/home#experiencia", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_proyectos, href="/home#proyectos", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_github, href="/home#github", on_click=State.limpiar_mensaje_formulario, color="white"), 
                rx.link(State.nav_formacion, href="/home#formacion", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_contacto, href="/home#contacto", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_cv, href="/cv", on_click=State.limpiar_mensaje_formulario, color="white"),
                spacing="6",
                class_name="navbar-links",
            ),
            rx.spacer(),
            selector_idioma(),
            # Icono hamburguesa (visible solo en móvil)
            rx.button(
                rx.icon("menu", size=28),
                on_click=State.toggle_menu,
                variant="ghost",
                color="white",
                class_name="hamburger-icon",
                _hover={"background": "transparent"},
            ),
            width="100%",
            align="center",
        ),
        # Menú móvil desplegable
        rx.cond(
            State.menu_abierto,
            rx.vstack(
                rx.link(
                    State.nav_inicio,
                    href="/home#inicio",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_sobre_mi,
                    href="/home#sobre-mi",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_experiencia,
                    href="/home#experiencia",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_proyectos,
                    href="/home#proyectos",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_github,  # ← AÑADIR ESTE BLOQUE COMPLETO
                    href="/home#github",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_contacto,
                    href="/home#contacto",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_cv,
                    href="/cv",
                    on_click=State.cerrar_menu_y_limpiar,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                spacing="0",
                width="100%",
                bg="#000000",
                position="absolute",
                top="4em",
                left="0",
                class_name="mobile-menu",
            ),
        ),
        bg="#000000",
        padding="1em 2em",
        width="100%",
        position="fixed",
        top="0",
        z_index="1000",
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
            # Habilidades técnicas (ahora al final)
            rx.heading(State.habilidades_titulo, size="6", color="white", margin_top="2em"),
            rx.hstack(
                rx.badge("Python", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("Reflex", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("FastAPI", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("JavaScript", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                rx.badge("Git", variant="outline", color_scheme="gray", style={"border_color": "white", "color": "white"}),
                spacing="3",
                wrap="wrap",
            ),
            
            spacing="4",
            align="center",
            text_align="center",
        ),
        padding="6em 2em",
        bg="#000000",
        width="100%",
        id="sobre-mi",
    )

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
                            # Tipo y empresa
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
                                                rx.cond(
                                                    State.idioma == "it",
                                                    exp.cargo_it,
                                                    exp.cargo_ca
                                                )
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
                            # Fechas
                            rx.hstack(
                                rx.icon("calendar", size=20, color="#CCCCCC"),
                                rx.text(
                                    rx.cond(
                                        exp.actual,
                                        f"{exp.fecha_inicio} - Actualidad",
                                        f"{exp.fecha_inicio} - {exp.fecha_fin}"
                                    ),
                                    size="3",
                                    color="#CCCCCC",
                                ),
                                spacing="2",
                            ),
                            # Descripción
                            rx.cond(
                                rx.cond(
                                    State.idioma == "es",
                                    exp.descripcion_es,
                                    rx.cond(
                                        State.idioma == "en",
                                        exp.descripcion_en,
                                        rx.cond(
                                            State.idioma == "it",
                                            exp.descripcion_it,
                                            exp.descripcion_ca
                                        )
                                    )
                                ) != "",
                                rx.text(
                                    rx.cond(
                                        State.idioma == "es",
                                        exp.descripcion_es,
                                        rx.cond(
                                            State.idioma == "en",
                                            exp.descripcion_en,
                                            rx.cond(
                                                State.idioma == "it",
                                                exp.descripcion_it,
                                                exp.descripcion_ca
                                            )
                                        )
                                    ),
                                    size="3",
                                    color="#CCCCCC",
                                    line_height="1.6",
                                ),
                            ),
                            # Tecnologías
                            rx.hstack(
                                rx.foreach(
                                    exp.tecnologias,
                                    lambda tech: rx.badge(tech, variant="outline", color_scheme="gray"),
                                ),
                                wrap="wrap",
                                spacing="2",
                            ),
                            spacing="4",
                            align="start",
                        ),
                        padding="1.5em",
                        border_radius="8px",
                        border="1px solid #333333",
                        bg="#0a0a0a",
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
        id="experiencia",
        padding="4em 2em",
        background_color="#000000",
    )

def skeleton_curso() -> rx.Component:
    """Skeleton loader para curso mientras carga"""
    return rx.box(
        rx.vstack(
            # Tipo y título skeleton
            rx.hstack(
                rx.box(
                    height="20px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="60%",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
            ),
            # Institución skeleton
            rx.box(
                height="16px",
                width="50%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            # Fechas skeleton
            rx.box(
                height="14px",
                width="40%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            spacing="2",
            align_items="start",
        ),
        padding="1.5em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
        width="100%",
    )


def skeleton_experiencia() -> rx.Component:
    """Skeleton loader para experiencia mientras carga"""
    return rx.box(
        rx.vstack(
            # Cargo y empresa skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="24px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.vstack(
                    rx.box(
                        height="20px",
                        width="200px",
                        bg="#1a1a1a",
                        border_radius="4px",
                        class_name="skeleton-pulse",
                    ),
                    rx.box(
                        height="16px",
                        width="150px",
                        bg="#1a1a1a",
                        border_radius="4px",
                        class_name="skeleton-pulse",
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="start",
            ),
            # Fechas skeleton
            rx.hstack(
                rx.box(
                    height="20px",
                    width="20px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="16px",
                    width="180px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="90%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Tecnologías skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="70px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
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
def skeleton_repo_github() -> rx.Component:
    """Skeleton loader para repo de GitHub mientras carga"""
    return rx.box(
        rx.vstack(
            # Nombre del repo skeleton
            rx.box(
                height="24px",
                width="60%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="80%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            # Stats skeleton (lenguaje, stars, forks)
            rx.hstack(
                rx.box(
                    height="20px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="20px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="20px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
                margin_top="1em",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="1.5em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
        width="100%",
    )


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


def skeleton_proyecto() -> rx.Component:
    """Skeleton loader para proyecto mientras carga"""
    return rx.box(
        rx.vstack(
            # Título skeleton
            rx.box(
                height="28px",
                width="70%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="85%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            # Badges skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="70px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="55px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
                margin_top="1em",
            ),
            # Botones skeleton
            rx.hstack(
                rx.box(
                    height="36px",
                    width="100px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="36px",
                    width="100px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
                margin_top="1em",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="2em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
    )

def seccion_proyectos() -> rx.Component:
    """Seccion Proyectos con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.proyectos_titulo, size="8", color="white"),
            
            rx.cond(
                State.cargando_proyectos,
                rx.box(
                    rx.hstack(
                        skeleton_proyecto(),
                        skeleton_proyecto(),
                        skeleton_proyecto(),
                        spacing="3",
                        wrap="wrap",
                    ),
                    class_name="proyectos-grid",
                    width="100%",
                ),
            ),
            
            rx.cond(
                State.error_proyectos != "",
                rx.text(State.error_proyectos, color="red"),
            ),
            
            rx.box(
                rx.foreach(
                    State.proyectos,
                    lambda proyecto: rx.box(
                        rx.vstack(
                            rx.heading(
                                rx.cond(
                                    State.idioma == "es",
                                    proyecto.titulo_es,
                                    rx.cond(
                                        State.idioma == "en",
                                        proyecto.titulo_en,
                                        rx.cond(
                                            State.idioma == "it",
                                            proyecto.titulo_it,
                                            proyecto.titulo_ca
                                        )
                                    )
                                ),
                                size="5",
                                color="white",
                            ),
                            rx.text(
                                rx.cond(
                                    State.idioma == "es",
                                    proyecto.descripcion_es,
                                    rx.cond(
                                        State.idioma == "en",
                                        proyecto.descripcion_en,
                                        rx.cond(
                                            State.idioma == "it",
                                            proyecto.descripcion_it,
                                            proyecto.descripcion_ca
                                        )
                                    )
                                ),
                                color="#CCCCCC",
                                size="2",
                            ),
                            rx.hstack(
                                rx.foreach(
                                    proyecto.tecnologias,
                                    lambda tech: rx.badge(tech, color_scheme="gray"),
                                ),
                                wrap="wrap",
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.cond(
                                    proyecto.github_url != "",
                                    rx.link(
                                        rx.button("Ver codigo", variant="outline"),
                                        href=proyecto.github_url,
                                        is_external=True,
                                    ),
                                ),
                                rx.cond(
                                    proyecto.demo_url != "",
                                    rx.link(
                                        rx.button("Ver demo", variant="solid"),
                                        href=proyecto.demo_url,
                                        is_external=True,
                                    ),
                                ),
                                spacing="3",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="2em",
                        border_radius="8px",
                        border="1px solid #333333",
                        background_color="#0A0A0A",
                        class_name="fade-in-up",
                    )
                ),
                class_name="proyectos-grid",
                width="100%",
            ),
            
            spacing="5",
            align_items="center",
            width="100%",
        ),
        id="proyectos",
        padding="4em 2em",
        background_color="#000000",
    )

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



def seccion_contacto() -> rx.Component:
    """Sección Contacto con información y formulario"""
    return rx.box(
        rx.vstack(
            rx.heading(State.contacto_titulo, size="8", color="white"),

            # Información de contacto
            rx.vstack(
                rx.heading(State.contacto_info_titulo, size="6", color="white", margin_bottom="1em"),
                rx.hstack(
                    rx.icon("mail", size=20, color="white"),
                    rx.text(State.contacto_email + ":", color="#cccccc", weight="bold"),
                    rx.link(
                        "alessandro.febbrai@ejemplo.com",
                        href="mailto:alessandro.febbrai@ejemplo.com",
                        color="white",
                        _hover={"color": "#808080"},
                    ),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon("phone", size=20, color="white"),
                    rx.text(State.contacto_telefono + ":", color="#cccccc", weight="bold"),
                    rx.text("+34 XXX XXX XXX", color="white"),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon("linkedin", size=20, color="white"),
                    rx.text(State.contacto_linkedin + ":", color="#cccccc", weight="bold"),
                    rx.link(
                        "/alessandro-febbrai",
                        href="https://linkedin.com/in/alessandro-febbrai",
                        is_external=True,
                        color="white",
                        _hover={"color": "#808080"},
                    ),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon("github", size=20, color="white"),
                    rx.text(State.contacto_github + ":", color="#cccccc", weight="bold"),
                    rx.link(
                        "/geobest7",
                        href="https://github.com/geobest7",
                        is_external=True,
                        color="white",
                        _hover={"color": "#808080"},
                    ),
                    spacing="2",
                ),
                spacing="3",
                align="start",
                margin_bottom="3em",
            ),
            
            # Subtítulo antes del formulario
            rx.text(State.contacto_subtitulo, color="#cccccc", size="4", margin_bottom="2em"),

            # Formulario de contacto
            rx.vstack(
                rx.input(
                    placeholder=State.form_nombre,
                    value=State.form_nombre_value,
                    on_change=State.set_nombre,
                    width="100%",
                    max_width="500px",
                    size="3",
                ),
                rx.input(
                    placeholder=State.form_email,
                    value=State.form_email_value,
                    on_change=State.set_email,
                    type="email",
                    width="100%",
                    max_width="500px",
                    size="3",
                ),
                rx.text_area(
                    placeholder=State.form_mensaje,
                    value=State.form_mensaje_value,
                    on_change=State.set_mensaje,
                    width="100%",
                    max_width="500px",
                    min_height="150px",
                    size="3",
                ),
                rx.button(
                    State.btn_enviar,
                    on_click=State.enviar_formulario,
                    loading=State.form_enviando,
                    size="3",
                    variant="solid",
                    color_scheme="gray",
                    style={"background": "white", "color": "black"},
                ),
                # Mensaje de éxito o error
                rx.cond(
                    State.form_mensaje_estado != "",
                    rx.box(
                        rx.text(
                            State.form_mensaje_texto,
                            color=rx.cond(
                                State.form_mensaje_estado == "exito",
                                "#00ff00",
                                "#ff0000",
                            ),
                            weight="bold",
                            size="3",
                        ),
                        padding="1em",
                        border_radius="8px",
                        bg=rx.cond(
                            State.form_mensaje_estado == "exito",
                            "#001a00",
                            "#1a0000",
                        ),
                        border=rx.cond(
                            State.form_mensaje_estado == "exito",
                            "1px solid #00ff00",
                            "1px solid #ff0000",
                        ),
                        max_width="500px",
                        width="100%",
                    ),
                ),
                spacing="4",
                width="100%",
                align="center",
            ),
            spacing="4",
            align="center",
            text_align="center",
        ),
        padding="6em 2em",
        bg="#000000",
        width="100%",
        id="contacto",
    )



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



def portada() -> rx.Component:
    """Página de portada - Solo selector de idioma"""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Alessandro Febbrai", size="9", color="white"),
                rx.text("Select language / Selecciona idioma / Seleziona lingua / Selecciona l'idioma", color="#808080", size="3", text_align="center"),
                selector_idioma_portada(),
                spacing="6",
            ),
        ),
        bg="#000000",
        color="white",
        min_height="100vh",
    )

def pagina_login() -> rx.Component:
    """Página de login para admin"""
    return rx.box(
        rx.vstack(
            # Logo o título
            rx.heading("Panel Admin", size="9", color="white", margin_bottom="2em"),
            
            # Formulario de login
            rx.form(
                rx.vstack(
                    rx.heading("Iniciar Sesión", size="6", color="white", margin_bottom="1em"),
                    
                    # Campo username
                    rx.vstack(
                        rx.text("Usuario", color="#CCCCCC", size="2"),
                        rx.input(
                            name="username",
                            placeholder="admin",
                            type="text",
                            width="100%",
                            size="3",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # Campo password
                    rx.vstack(
                        rx.text("Contraseña", color="#CCCCCC", size="2"),
                        rx.input(
                            name="password",
                            placeholder="••••••••",
                            type="password",
                            width="100%",
                            size="3",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # Mensaje de error
                    rx.cond(
                        State.error_login != "",
                        rx.text(
                            State.error_login,
                            color="red",
                            size="2",
                        ),
                    ),
                    
                    # Botón login
                    rx.button(
                        rx.cond(
                            State.cargando_login,
                            rx.spinner(size="3"),
                            rx.text("Iniciar Sesión"),
                        ),
                        type="submit",
                        width="100%",
                        size="3",
                        color_scheme="cyan",
                    ),
                    
                    spacing="4",
                    width="100%",
                ),
                on_submit=State.login,
                width="100%",
                max_width="400px",
                padding="2em",
                border_radius="8px",
                background="#1a1a1a",
                box_shadow="0 4px 6px rgba(0, 0, 0, 0.3)",
            ),
            
            spacing="6",
            align="center",
            justify="center",
            min_height="100vh",
        ),
        bg="#000000",
        width="100%",
    )

def dashboard_admin() -> rx.Component:
    """Dashboard principal del panel admin"""
    return rx.cond(
        State.esta_autenticado,
        # Usuario autenticado - mostrar dashboard
        rx.box(
            # Header admin
            rx.box(
                rx.hstack(
                    rx.heading("Panel Admin", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.text(
                            f"Bienvenido, {State.usuario_autenticado.get('username', 'Admin')}",
                            color="#CCCCCC",
                            size="3",
                        ),
                        rx.button(
                            "Cerrar Sesión",
                            on_click=State.logout,
                            variant="outline",
                            color_scheme="red",
                            size="2",
                        ),
                        spacing="4",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Contenido principal
            rx.box(
                rx.vstack(
                    # Tarjetas de navegación
                    rx.heading("Gestión de Contenido", size="6", color="white", margin_bottom="1em"),
                    
                    rx.grid(
                        # Card Proyectos
                        rx.box(
                            rx.vstack(
                                rx.icon("folder-git", size=40, color="#00CED1"),
                                rx.heading("Proyectos", size="5", color="white"),
                                rx.text(
                                    "Gestionar proyectos del portfolio",
                                    color="#CCCCCC",
                                    size="2",
                                    text_align="center",
                                ),
                                rx.button(
                                    "Administrar",
                                    on_click=rx.redirect("/admin/proyectos"),
                                    width="100%",
                                    color_scheme="cyan",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            padding="2em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                            _hover={"border_color": "#00CED1"},
                        ),
                        
                        # Card Cursos
                        rx.box(
                            rx.vstack(
                                rx.icon("graduation-cap", size=40, color="#00CED1"),
                                rx.heading("Cursos", size="5", color="white"),
                                rx.text(
                                    "Gestionar cursos y certificaciones",
                                    color="#CCCCCC",
                                    size="2",
                                    text_align="center",
                                ),
                                rx.button(
                                    "Administrar",
                                    on_click=rx.redirect("/admin/cursos"),
                                    width="100%",
                                    color_scheme="cyan",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            padding="2em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                            _hover={"border_color": "#00CED1"},
                        ),
                        
                        # Card Experiencias
                        rx.box(
                            rx.vstack(
                                rx.icon("briefcase", size=40, color="#00CED1"),
                                rx.heading("Experiencias", size="5", color="white"),
                                rx.text(
                                    "Gestionar experiencia laboral",
                                    color="#CCCCCC",
                                    size="2",
                                    text_align="center",
                                ),
                                rx.button(
                                    "Administrar",
                                    on_click=rx.redirect("/admin/experiencias"),
                                    width="100%",
                                    color_scheme="cyan",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            padding="2em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                            _hover={"border_color": "#00CED1"},
                        ),
                        
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    
                    # Link al portfolio
                    rx.divider(margin_top="2em", margin_bottom="2em"),
                    rx.link(
                        rx.hstack(
                            rx.icon("external-link", size=20),
                            rx.text("Ver Portfolio Público", size="3"),
                            spacing="2",
                        ),
                        href="/home",
                        color="#00CED1",
                        _hover={"color": "#00FFFF"},
                    ),
                    
                    spacing="4",
                    width="100%",
                    max_width="1200px",
                ),
                padding="2em",
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        # No autenticado - redirigir a login
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )

def admin_proyectos() -> rx.Component:
    """Página de administración de proyectos"""
    return rx.cond(
        State.esta_autenticado,
        # Usuario autenticado
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Proyectos", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("arrow-left", size=20),
                                rx.text("Volver"),
                                spacing="2",
                            ),
                            on_click=rx.redirect("/admin"),
                            variant="outline",
                            size="2",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("plus", size=20),
                                rx.text("Nuevo Proyecto"),
                                spacing="2",
                            ),
                            on_click=lambda: State.abrir_formulario_proyecto(0),
                            color_scheme="cyan",
                            size="2",
                        ),
                        spacing="3",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Contenido
            rx.box(
                rx.cond(
                    State.cargando_proyectos_admin,
                    rx.center(
                        rx.spinner(size="3"),
                        padding="4em",
                    ),
                    rx.cond(
                        State.error_proyectos_admin != "",
                        rx.text(State.error_proyectos_admin, color="red"),
                        # Tabla de proyectos
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Título (ES)"),
                                    rx.table.column_header_cell("Destacado"),
                                    rx.table.column_header_cell("Activo"),
                                    rx.table.column_header_cell("Orden"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.proyectos_admin,
                                    lambda proyecto: rx.table.row(
                                        rx.table.cell(proyecto.id),
                                        rx.table.cell(proyecto.titulo_es),
                                        rx.table.cell(
                                            rx.cond(
                                                proyecto.destacado,
                                                rx.badge("Sí", color_scheme="green"),
                                                rx.badge("No", color_scheme="gray"),
                                            ),
                                        ),
                                        rx.table.cell(
                                            rx.cond(
                                                proyecto.activo,
                                                rx.badge("Activo", color_scheme="blue"),
                                                rx.badge("Inactivo", color_scheme="red"),
                                            ),
                                        ),
                                        rx.table.cell(proyecto.orden),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(
                                                    rx.icon("pencil", size=16),
                                                    on_click=State.abrir_formulario_proyecto(proyecto.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                rx.button(
                                                    rx.icon("trash-2", size=16),
                                                    on_click=State.eliminar_proyecto(proyecto.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="red",
                                                ),
                                                spacing="2",
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            variant="surface",
                            size="3",
                        ),
                    ),
                ),
                padding="2em",
                on_mount=State.cargar_proyectos_admin,
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        # No autenticado
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )


def formulario_proyecto() -> rx.Component:
    """Formulario para crear/editar proyecto"""
    return rx.cond(
        State.esta_autenticado,
        # Usuario autenticado
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading(
                        rx.cond(
                            State.modo_edicion,
                            "Editar Proyecto",
                            "Nuevo Proyecto",
                        ),
                        size="7",
                        color="white",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("x", size=20),
                            rx.text("Cancelar"),
                            spacing="2",
                        ),
                        on_click=State.cancelar_edicion_proyecto,
                        variant="outline",
                        size="2",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Formulario
            rx.box(
                rx.form(
                    rx.vstack(
                        # Títulos en 4 idiomas
                        rx.heading("Títulos", size="5", color="white", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Título (ES)", color="#CCC", size="2"),
                                rx.input(
                                    name="titulo_es",
                                    placeholder="Título en español",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_es, ""),
                                    required=True,
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (EN)", color="#CCC", size="2"),
                                rx.input(
                                    name="titulo_en",
                                    placeholder="Title in English",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_en, ""),
                                    required=True,
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (IT)", color="#CCC", size="2"),
                                rx.input(
                                    name="titulo_it",
                                    placeholder="Titolo in italiano",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_it, ""),
                                    required=True,
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (CA)", color="#CCC", size="2"),
                                rx.input(
                                    name="titulo_ca",
                                    placeholder="Títol en català",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_ca, ""),
                                    required=True,
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            columns="2",
                            spacing="4",
                            width="100%",
                        ),
                        
                        # Descripciones en 4 idiomas
                        rx.heading("Descripciones", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Descripción (ES)", color="#CCC", size="2"),
                                rx.text_area(
                                    name="descripcion_es",
                                    placeholder="Descripción en español",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_es, ""),
                                    required=True,
                                    width="100%",
                                    rows="4",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (EN)", color="#CCC", size="2"),
                                rx.text_area(
                                    name="descripcion_en",
                                    placeholder="Description in English",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_en, ""),
                                    required=True,
                                    width="100%",
                                    rows="4",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (IT)", color="#CCC", size="2"),
                                rx.text_area(
                                    name="descripcion_it",
                                    placeholder="Descrizione in italiano",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_it, ""),
                                    required=True,
                                    width="100%",
                                    rows="4",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (CA)", color="#CCC", size="2"),
                                rx.text_area(
                                    name="descripcion_ca",
                                    placeholder="Descripció en català",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_ca, ""),
                                    required=True,
                                    width="100%",
                                    rows="4",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            columns="2",
                            spacing="4",
                            width="100%",
                        ),
                        
                        # Tecnologías, URLs y configuración
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Tecnologías (separadas por coma)", color="#CCC", size="2"),
                                rx.input(
                                    name="tecnologias",
                                    placeholder="Python,FastAPI,Reflex",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.tecnologias.join(","), ""),
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL GitHub", color="#CCC", size="2"),
                                rx.input(
                                    name="github_url",
                                    placeholder="https://github.com/...",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.github_url, ""),
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL Demo", color="#CCC", size="2"),
                                rx.input(
                                    name="demo_url",
                                    placeholder="https://...",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.demo_url, ""),
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL Imagen", color="#CCC", size="2"),
                                rx.input(
                                    name="imagen_url",
                                    placeholder="https://...",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.imagen_url, ""),
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Orden", color="#CCC", size="2"),
                                rx.input(
                                    name="orden",
                                    type="number",
                                    placeholder="0",
                                    default_value=rx.cond(State.modo_edicion, State.proyecto_editando.orden.to_string(), "0"),
                                    width="100%",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Destacado", color="#CCC", size="2"),
                                rx.checkbox(
                                    name="destacado",
                                    default_checked=rx.cond(State.modo_edicion, State.proyecto_editando.destacado, False),
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            columns="3",
                            spacing="4",
                            width="100%",
                        ),
                        
                        # Botón guardar
                        rx.button(
                            rx.cond(
                                State.modo_edicion,
                                "Actualizar Proyecto",
                                "Crear Proyecto",
                            ),
                            type="submit",
                            size="3",
                            color_scheme="cyan",
                            width="100%",
                            margin_top="2em",
                        ),
                        
                        spacing="4",
                        width="100%",
                        max_width="1200px",
                    ),
                    on_submit=State.guardar_proyecto,
                    width="100%",
                ),
                padding="2em",
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        # No autenticado
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )



def admin_cursos() -> rx.Component:
    """Página de administración de cursos"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Cursos", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("arrow-left", size=20),
                                rx.text("Volver"),
                                spacing="2",
                            ),
                            on_click=rx.redirect("/admin"),
                            variant="outline",
                            size="2",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("plus", size=20),
                                rx.text("Nuevo Curso"),
                                spacing="2",
                            ),
                            on_click=lambda: State.abrir_formulario_curso(0),
                            color_scheme="cyan",
                            size="2",
                        ),
                        spacing="3",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Contenido
            rx.box(
                rx.cond(
                    State.cargando_cursos_admin,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    rx.cond(
                        State.error_cursos_admin != "",
                        rx.text(State.error_cursos_admin, color="red"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Título (ES)"),
                                    rx.table.column_header_cell("Institución (ES)"),
                                    rx.table.column_header_cell("Fecha Inicio"),
                                    rx.table.column_header_cell("Activo"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.cursos_admin,
                                    lambda curso: rx.table.row(
                                        rx.table.cell(curso.id),
                                        rx.table.cell(curso.titulo_es),
                                        rx.table.cell(curso.institucion_es),
                                        rx.table.cell(curso.fecha_inicio),
                                        rx.table.cell(
                                            rx.cond(
                                                curso.activo,
                                                rx.badge("Activo", color_scheme="blue"),
                                                rx.badge("Inactivo", color_scheme="red"),
                                            ),
                                        ),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(
                                                    rx.icon("pencil", size=16),
                                                    on_click=State.abrir_formulario_curso(curso.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                rx.button(
                                                    rx.icon("trash-2", size=16),
                                                    on_click=State.eliminar_curso(curso.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="red",
                                                ),
                                                spacing="2",
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            variant="surface",
                            size="3",
                        ),
                    ),
                ),
                padding="2em",
                on_mount=State.cargar_cursos_admin,
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )

def formulario_curso() -> rx.Component:
    """Formulario para crear/editar curso"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading(
                        rx.cond(
                            State.modo_edicion_curso,
                            "Editar Curso",
                            "Nuevo Curso",
                        ),
                        size="7",
                        color="white",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("x", size=20),
                            rx.text("Cancelar"),
                            spacing="2",
                        ),
                        on_click=State.cancelar_edicion_curso,
                        variant="outline",
                        size="2",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Formulario
            rx.box(
                rx.form(
                    rx.vstack(
                        # Títulos
                        rx.heading("Títulos", size="5", color="white", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Título (ES)", color="#CCC", size="2"),
                                rx.input(name="titulo_es", placeholder="Título en español", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_es, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (EN)", color="#CCC", size="2"),
                                rx.input(name="titulo_en", placeholder="Title in English", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_en, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (IT)", color="#CCC", size="2"),
                                rx.input(name="titulo_it", placeholder="Titolo in italiano", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_it, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (CA)", color="#CCC", size="2"),
                                rx.input(name="titulo_ca", placeholder="Títol en català", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_ca, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        
                        # Instituciones
                        rx.heading("Instituciones", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Institución (ES)", color="#CCC", size="2"),
                                rx.input(name="institucion_es", placeholder="Institución en español", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_es, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Institución (EN)", color="#CCC", size="2"),
                                rx.input(name="institucion_en", placeholder="Institution in English", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_en, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Institución (IT)", color="#CCC", size="2"),
                                rx.input(name="institucion_it", placeholder="Istituzione in italiano", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_it, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Institución (CA)", color="#CCC", size="2"),
                                rx.input(name="institucion_ca", placeholder="Institució en català", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_ca, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        
                        # Fechas y certificado
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Fecha Inicio", color="#CCC", size="2"),
                                rx.input(name="fecha_inicio", type="date", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.fecha_inicio, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Fecha Fin (opcional)", color="#CCC", size="2"),
                                rx.input(name="fecha_fin", type="date", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.fecha_fin, ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL Certificado (opcional)", color="#CCC", size="2"),
                                rx.input(name="certificado_url", placeholder="https://...", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.certificado_url, ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="3", spacing="4", width="100%",
                        ),
                        
                        # Botón guardar
                        rx.button(
                            rx.cond(State.modo_edicion_curso, "Actualizar Curso", "Crear Curso"),
                            type="submit",
                            size="3",
                            color_scheme="cyan",
                            width="100%",
                            margin_top="2em",
                        ),
                        
                        spacing="4", width="100%", max_width="1200px",
                    ),
                    on_submit=State.guardar_curso,
                    width="100%",
                ),
                padding="2em",
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )

def admin_experiencias() -> rx.Component:
    """Página de administración de experiencias"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Experiencias", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("arrow-left", size=20),
                                rx.text("Volver"),
                                spacing="2",
                            ),
                            on_click=rx.redirect("/admin"),
                            variant="outline",
                            size="2",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("plus", size=20),
                                rx.text("Nueva Experiencia"),
                                spacing="2",
                            ),
                            on_click=lambda: State.abrir_formulario_experiencia(0),
                            color_scheme="cyan",
                            size="2",
                        ),
                        spacing="3",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Contenido
            rx.box(
                rx.cond(
                    State.cargando_experiencias_admin,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    rx.cond(
                        State.error_experiencias_admin != "",
                        rx.text(State.error_experiencias_admin, color="red"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Tipo"),
                                    rx.table.column_header_cell("Empresa"),
                                    rx.table.column_header_cell("Cargo (ES)"),
                                    rx.table.column_header_cell("Fecha Inicio"),
                                    rx.table.column_header_cell("Mostrar Web"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.experiencias_admin,
                                    lambda exp: rx.table.row(
                                        rx.table.cell(exp.id),
                                        rx.table.cell(exp.tipo),
                                        rx.table.cell(exp.empresa),
                                        rx.table.cell(exp.cargo_es),
                                        rx.table.cell(exp.fecha_inicio),
                                        rx.table.cell(
                                            rx.cond(
                                                exp.mostrar_en_web,
                                                rx.badge("Sí", color_scheme="green"),
                                                rx.badge("No", color_scheme="gray"),
                                            ),
                                        ),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(
                                                    rx.icon("pencil", size=16),
                                                    on_click=State.abrir_formulario_experiencia(exp.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                rx.button(
                                                    rx.icon("trash-2", size=16),
                                                    on_click=State.eliminar_experiencia(exp.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="red",
                                                ),
                                                spacing="2",
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            variant="surface",
                            size="3",
                        ),
                    ),
                ),
                padding="2em",
                on_mount=State.cargar_experiencias_admin,
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )


def formulario_experiencia() -> rx.Component:
    """Formulario para crear/editar experiencia"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.heading(
                        rx.cond(
                            State.modo_edicion_experiencia,
                            "Editar Experiencia",
                            "Nueva Experiencia",
                        ),
                        size="7",
                        color="white",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("x", size=20),
                            rx.text("Cancelar"),
                            spacing="2",
                        ),
                        on_click=State.cancelar_edicion_experiencia,
                        variant="outline",
                        size="2",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            
            # Formulario
            rx.box(
                rx.form(
                    rx.vstack(
                        # Tipo y Empresa
                        rx.heading("Información General", size="5", color="white", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Tipo", color="#CCC", size="2"),
                                rx.select(["practica", "trabajo"], name="tipo", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.tipo, "practica"), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Empresa", color="#CCC", size="2"),
                                rx.input(name="empresa", placeholder="Nombre de la empresa", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.empresa, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        
                        # Cargos en 4 idiomas
                        rx.heading("Cargos", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Cargo (ES)", color="#CCC", size="2"),
                                rx.input(name="cargo_es", placeholder="Cargo en español", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_es, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Cargo (EN)", color="#CCC", size="2"),
                                rx.input(name="cargo_en", placeholder="Position in English", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_en, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Cargo (IT)", color="#CCC", size="2"),
                                rx.input(name="cargo_it", placeholder="Posizione in italiano", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_it, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Cargo (CA)", color="#CCC", size="2"),
                                rx.input(name="cargo_ca", placeholder="Càrrec en català", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_ca, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        
                        # Descripciones en 4 idiomas
                        rx.heading("Descripciones (opcional)", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Descripción (ES)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_es", placeholder="Descripción en español", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_es, ""), width="100%", rows="3"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (EN)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_en", placeholder="Description in English", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_en, ""), width="100%", rows="3"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (IT)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_it", placeholder="Descrizione in italiano", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_it, ""), width="100%", rows="3"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (CA)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_ca", placeholder="Descripció en català", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_ca, ""), width="100%", rows="3"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        
                        # Fechas, tecnologías y opciones
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Fecha Inicio", color="#CCC", size="2"),
                                rx.input(name="fecha_inicio", type="date", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.fecha_inicio, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Fecha Fin (opcional)", color="#CCC", size="2"),
                                rx.input(name="fecha_fin", type="date", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.fecha_fin, ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Tecnologías (separadas por coma)", color="#CCC", size="2"),
                                rx.input(name="tecnologias", placeholder="Python,FastAPI,React", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.tecnologias.join(","), ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Orden", color="#CCC", size="2"),
                                rx.input(name="orden", type="number", placeholder="0", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.orden.to_string(), "0"), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Trabajo Actual", color="#CCC", size="2"),
                                rx.checkbox(name="actual", default_checked=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.actual, False)),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Mostrar en Web", color="#CCC", size="2"),
                                rx.checkbox(name="mostrar_en_web", default_checked=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.mostrar_en_web, False)),
                                spacing="1", width="100%",
                            ),
                            columns="3", spacing="4", width="100%",
                        ),
                        
                        # Botón guardar
                        rx.button(
                            rx.cond(State.modo_edicion_experiencia, "Actualizar Experiencia", "Crear Experiencia"),
                            type="submit",
                            size="3",
                            color_scheme="cyan",
                            width="100%",
                            margin_top="2em",
                        ),
                        
                        spacing="4", width="100%", max_width="1200px",
                    ),
                    on_submit=State.guardar_experiencia,
                    width="100%",
                ),
                padding="2em",
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )



def home() -> rx.Component:
    """Página Home - Contenido principal del portfolio"""
    return rx.box(
        navbar(),
        rx.vstack(
            rx.image(
                src="/foto_perfil.png",
                width="150px",
                height="150px",
                border_radius="50%",
                margin_bottom="1em",
            ),
            rx.heading(State.hero_titulo, size="9"),
            rx.text(State.hero_subtitulo, size="5"),
            rx.text(State.hero_descripcion),
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

app = rx.App(
    stylesheets=[
        "styles/styles.css",
    ],
)
app.add_page(portada, route="/")
app.add_page(home, route="/home")
app.add_page(pagina_cv, route="/cv")
app.add_page(pagina_login, route="/login")
app.add_page(dashboard_admin, route="/admin")
app.add_page(admin_proyectos, route="/admin/proyectos")
app.add_page(formulario_proyecto, route="/admin/proyectos/form")
app.add_page(admin_cursos, route="/admin/cursos")
app.add_page(formulario_curso, route="/admin/cursos/form")
app.add_page(admin_experiencias, route="/admin/experiencias")
app.add_page(formulario_experiencia, route="/admin/experiencias/form")