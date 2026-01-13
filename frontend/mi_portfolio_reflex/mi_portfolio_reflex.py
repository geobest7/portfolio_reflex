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
            rx.heading("AF", size="7", color="white"),
            rx.spacer(),
            # Links desktop (ocultos en móvil)
            rx.hstack(
                rx.link(State.nav_inicio, href="/home#inicio", color="white"),
                rx.link(State.nav_sobre_mi, href="/home#sobre-mi", color="white"),
                rx.link(State.nav_proyectos, href="/home#proyectos", color="white"),
                rx.link(State.nav_contacto, href="/home#contacto", color="white"),
                rx.link(State.nav_cv, href="/cv", color="white"),
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
                    on_click=State.cerrar_menu,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_sobre_mi,
                    href="/home#sobre-mi",
                    on_click=State.cerrar_menu,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_proyectos,
                    href="/home#proyectos",
                    on_click=State.cerrar_menu,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_contacto,
                    href="/home#contacto",
                    on_click=State.cerrar_menu,
                    color="white",
                    width="100%",
                    padding="1em",
                    _hover={"background": "#1a1a1a"},
                ),
                rx.link(
                    State.nav_cv,
                    href="/cv",
                    on_click=State.cerrar_menu,
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



def card_proyecto(titulo: str, descripcion: str) -> rx.Component:
    """Card individual de proyecto"""
    return rx.box(
        rx.vstack(
            rx.heading(titulo, size="5", color="white"),
            rx.text(descripcion, color="#cccccc", size="3", line_height="1.6"),
            rx.button(
                State.btn_ver_codigo,
                variant="outline",
                color_scheme="gray",
                style={"border_color": "white", "color": "white"},
            ),
            spacing="3",
            align="start",
        ),
        padding="2em",
        border="1px solid #333333",
        border_radius="8px",
        bg="#0a0a0a",
        width="100%",
        max_width="350px",
    )


def seccion_proyectos() -> rx.Component:
    """Sección Proyectos con grid de cards"""
    return rx.box(
        rx.vstack(
            rx.heading(State.proyectos_titulo, size="8", color="white", margin_bottom="2em"),
            rx.flex(
                card_proyecto(State.proyecto_1_titulo, State.proyecto_1_desc),
                card_proyecto(State.proyecto_2_titulo, State.proyecto_2_desc),
                card_proyecto(State.proyecto_3_titulo, State.proyecto_3_desc),
                spacing="4",
                wrap="wrap",
                justify="center",
                class_name="proyectos-grid",
            ),
            spacing="4",
            align="center",
        ),
        padding="6em 2em",
        bg="#000000",
        width="100%",
        id="proyectos",
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


def home() -> rx.Component:
    """Página home - Con navbar y contenido"""
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.hero_titulo, size="9"),
            rx.text(State.hero_subtitulo, size="5"),
            rx.text(State.hero_descripcion),
            padding="4em 2em",
            padding_top="6em",
            spacing="4",
            id="inicio"
        ),
        seccion_sobre_mi(),
        seccion_proyectos(),
        seccion_contacto(),
        footer(),
        bg="#000000",
        color="white",
        min_height="100vh",
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