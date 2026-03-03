import reflex as rx
from ..states import State


def _contact_item(icon: str, label, value: str, href: str, external: bool = False) -> rx.Component:
    """Item de contacto con icono"""
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=18, color="white"),
            width="36px",
            height="36px",
            border_radius="8px",
            bg="rgba(255,255,255,0.06)",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(label, color="#666", size="1", font_weight="500"),
            rx.link(
                value,
                href=href,
                is_external=external,
                color="white",
                size="2",
                _hover={"color": "#ccc"},
            ),
            spacing="0",
            align="start",
        ),
        spacing="3",
        align="center",
    )


def seccion_contacto() -> rx.Component:
    """Sección Contacto con layout 2 columnas"""
    return rx.box(
        rx.vstack(
            rx.heading(State.contacto_titulo, size="8", color="white", text_align="center", width="100%"),
            rx.text(State.contacto_subtitulo, color="#999", size="4", text_align="center", max_width="600px"),
            rx.box(
                rx.hstack(
                    # Columna izquierda: info de contacto
                    rx.vstack(
                        rx.heading(State.contacto_info_titulo, size="5", color="white", margin_bottom="0.5em"),
                        _contact_item("mail", State.contacto_email, "febbrai.alessandro@libero.it", "mailto:febbrai.alessandro@libero.it"),
                        _contact_item("phone", State.contacto_telefono, "+34 632 172 521", "tel:+34632172521"),
                        _contact_item("linkedin", State.contacto_linkedin, "Alessandro Febbrai", "https://www.linkedin.com/in/alessandro-febbrai-b239021a2", True),
                        _contact_item("github", State.contacto_github, "geobest7", "https://github.com/geobest7", True),
                        spacing="4",
                        align="start",
                        flex="1",
                        min_width="280px",
                    ),
                    # Columna derecha: formulario
                    rx.vstack(
                        rx.input(
                            placeholder=State.form_nombre,
                            value=State.form_nombre_value,
                            on_change=State.set_nombre,
                            width="100%",
                            size="3",
                        ),
                        rx.input(
                            placeholder=State.form_email,
                            value=State.form_email_value,
                            on_change=State.set_email,
                            type="email",
                            width="100%",
                            size="3",
                        ),
                        rx.text_area(
                            placeholder=State.form_mensaje,
                            value=State.form_mensaje_value,
                            on_change=State.set_mensaje,
                            width="100%",
                            min_height="130px",
                            size="3",
                        ),
                        rx.button(
                            State.btn_enviar,
                            on_click=State.enviar_formulario,
                            loading=State.form_enviando,
                            disabled=(State.form_nombre_value == "") | (State.form_email_value == "") | (State.form_mensaje_value == ""),
                            size="3",
                            width="100%",
                            style={"background": "white", "color": "black", "font-weight": "600"},
                            _hover={"opacity": "0.9"},
                            _disabled={"opacity": "0.4", "cursor": "not-allowed"},
                        ),
                        rx.cond(
                            State.form_mensaje_estado != "",
                            rx.box(
                                rx.text(
                                    State.form_mensaje_texto,
                                    color=rx.cond(State.form_mensaje_estado == "exito", "#4ade80", "#f87171"),
                                    weight="bold",
                                    size="2",
                                ),
                                padding="0.8em",
                                border_radius="8px",
                                bg=rx.cond(State.form_mensaje_estado == "exito", "rgba(74,222,128,0.08)", "rgba(248,113,113,0.08)"),
                                border=rx.cond(State.form_mensaje_estado == "exito", "1px solid rgba(74,222,128,0.3)", "1px solid rgba(248,113,113,0.3)"),
                                width="100%",
                            ),
                        ),
                        spacing="3",
                        flex="1",
                        min_width="300px",
                    ),
                    spacing="8",
                    width="100%",
                    max_width="900px",
                    wrap="wrap",
                    align="start",
                ),
                width="100%",
                display="flex",
                justify_content="center",
                margin_top="2em",
            ),
            spacing="4",
            align="center",
        ),
        padding="6em 2em",
        bg="#000000",
        width="100%",
        id="contacto",
    )
