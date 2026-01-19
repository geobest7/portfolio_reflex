import reflex as rx
from ..states import State


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
