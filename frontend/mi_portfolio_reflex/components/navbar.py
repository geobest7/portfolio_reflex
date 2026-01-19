import reflex as rx
from ..states import State
from .selectors import selector_idioma


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
                    State.nav_github,
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
