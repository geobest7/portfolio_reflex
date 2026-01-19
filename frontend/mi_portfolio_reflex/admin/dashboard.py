import reflex as rx
from ..states import State


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
