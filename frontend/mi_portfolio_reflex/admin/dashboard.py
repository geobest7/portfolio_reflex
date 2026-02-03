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
                    
                    # Sección Configuración de Cuenta
                    rx.divider(margin_top="2em", margin_bottom="1em"),
                    rx.heading("Configuración de Cuenta", size="6", color="white", margin_bottom="1em"),
                    
                    rx.hstack(
                        # Botón cambiar contraseña
                        rx.button(
                            rx.hstack(
                                rx.icon("lock", size=18),
                                rx.text("Cambiar Contraseña"),
                                spacing="2",
                            ),
                            on_click=State.abrir_modal_password,
                            color_scheme="orange",
                            variant="outline",
                        ),
                        # Botón cambiar username
                        rx.button(
                            rx.hstack(
                                rx.icon("user", size=18),
                                rx.text("Cambiar Usuario"),
                                spacing="2",
                            ),
                            on_click=State.abrir_modal_username,
                            color_scheme="purple",
                            variant="outline",
                        ),
                        spacing="4",
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
            
            # Modal Cambiar Contraseña
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title("Cambiar Contraseña"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                name="current_password",
                                placeholder="Contraseña actual",
                                type="password",
                                width="100%",
                            ),
                            rx.input(
                                name="new_password",
                                placeholder="Nueva contraseña (mín. 6 caracteres)",
                                type="password",
                                width="100%",
                            ),
                            rx.cond(
                                State.error_cambio != "",
                                rx.text(State.error_cambio, color="red", size="2"),
                            ),
                            rx.hstack(
                                rx.button(
                                    "Cancelar",
                                    type="button",
                                    variant="outline",
                                    color_scheme="gray",
                                    on_click=State.cerrar_modal_password,
                                ),
                                rx.button(
                                    rx.cond(
                                        State.cargando_cambio,
                                        rx.spinner(size="2"),
                                        rx.text("Guardar"),
                                    ),
                                    type="submit",
                                    color_scheme="orange",
                                ),
                                spacing="3",
                                justify="end",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=State.cambiar_password,
                    ),
                    style={"max_width": "400px"},
                ),
                open=State.mostrar_modal_password,
            ),
            
            # Modal Cambiar Username
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title("Cambiar Usuario"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                name="new_username",
                                placeholder="Nuevo nombre de usuario (mín. 3 caracteres)",
                                type="text",
                                width="100%",
                            ),
                            rx.input(
                                name="password",
                                placeholder="Contraseña actual (para confirmar)",
                                type="password",
                                width="100%",
                            ),
                            rx.cond(
                                State.error_cambio != "",
                                rx.text(State.error_cambio, color="red", size="2"),
                            ),
                            rx.hstack(
                                rx.button(
                                    "Cancelar",
                                    type="button",
                                    variant="outline",
                                    color_scheme="gray",
                                    on_click=State.cerrar_modal_username,
                                ),
                                rx.button(
                                    rx.cond(
                                        State.cargando_cambio,
                                        rx.spinner(size="2"),
                                        rx.text("Guardar"),
                                    ),
                                    type="submit",
                                    color_scheme="purple",
                                ),
                                spacing="3",
                                justify="end",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=State.cambiar_username,
                    ),
                    style={"max_width": "400px"},
                ),
                open=State.mostrar_modal_username,
            ),
            
            bg="#000000",
            min_height="100vh",
        ),
        # No autenticado - redirigir a login
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )
