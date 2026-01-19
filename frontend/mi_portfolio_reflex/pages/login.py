import reflex as rx
from ..states import State


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
