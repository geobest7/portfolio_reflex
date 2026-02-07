import reflex as rx
from ..states import State
from .selectors import selector_idioma


def _mobile_link(label, href, on_click) -> rx.Component:
    """Link reutilizable para menú móvil"""
    return rx.link(
        label,
        href=href,
        on_click=on_click,
        color="white",
        width="100%",
        padding="1em",
        _hover={"background": "#1a1a1a"},
    )


def navbar() -> rx.Component:
    """Barra de navegación con links y selector de idioma"""
    return rx.box(
        rx.hstack(
            # Logo AF
            rx.box(
                rx.text(
                    "AF",
                    font_size="20px",
                    font_weight="800",
                    color="white",
                    letter_spacing="-0.05em",
                ),
                width="45px",
                height="45px",
                border_radius="50%",
                bg="linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%)",
                border="2px solid #EEEEEE",
                display="flex",
                align_items="center",
                justify_content="center",
                cursor="pointer",
                _hover={"border_color": "#FFFFFF", "transform": "scale(1.05)"},
                transition="all 0.2s ease",
                aria_label="Alessandro Febbrai",
                flex_shrink="0",
            ),
            # Links desktop (ocultos en móvil via CSS)
            rx.hstack(
                rx.link(State.nav_inicio, href="/home#inicio", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_sobre_mi, href="/home#sobre-mi", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_experiencia, href="/home#experiencia", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_formacion, href="/home#formacion", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_proyectos, href="/home#proyectos", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_github, href="/home#github", on_click=State.limpiar_mensaje_formulario, color="white"), 
                rx.link(State.nav_contacto, href="/home#contacto", on_click=State.limpiar_mensaje_formulario, color="white"),
                rx.link(State.nav_cv, href="/cv", on_click=State.limpiar_mensaje_formulario, color="white"),
                spacing="6",
                class_name="navbar-links",
                flex="1",
                justify="center",
            ),
            # Selector idioma desktop (oculto en móvil via CSS)
            rx.box(
                selector_idioma(),
                class_name="navbar-lang-desktop",
                flex_shrink="0",
            ),
            # Icono hamburguesa (visible solo en móvil via CSS)
            rx.button(
                rx.icon("menu", size=28),
                on_click=State.toggle_menu,
                variant="ghost",
                color="white",
                class_name="hamburger-icon",
                _hover={"background": "transparent"},
                flex_shrink="0",
                padding="0",
                min_width="auto",
            ),
            width="100%",
            max_width="100%",
            align="center",
            justify="between",
            overflow="hidden",
        ),
        # Menú móvil desplegable
        rx.cond(
            State.menu_abierto,
            rx.vstack(
                _mobile_link(State.nav_inicio, "/home#inicio", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_sobre_mi, "/home#sobre-mi", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_experiencia, "/home#experiencia", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_proyectos, "/home#proyectos", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_github, "/home#github", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_contacto, "/home#contacto", State.cerrar_menu_y_limpiar),
                _mobile_link(State.nav_cv, "/cv", State.cerrar_menu_y_limpiar),
                # Selector idioma dentro del menú móvil
                rx.hstack(
                    selector_idioma(),
                    padding="1em",
                    width="100%",
                    justify="center",
                ),
                spacing="0",
                width="100%",
                bg="#000000",
                position="absolute",
                top="100%",
                left="0",
                class_name="mobile-menu",
                z_index="999",
            ),
        ),
        bg="#000000",
        padding="0.8em 1em",
        margin="0",
        width="100%",
        max_width="100vw",
        position="fixed",
        top="0",
        left="0",
        z_index="1000",
        box_sizing="border-box",
    )
