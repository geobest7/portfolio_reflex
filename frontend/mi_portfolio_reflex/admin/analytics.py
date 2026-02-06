import reflex as rx
from ..states import State


def admin_analytics() -> rx.Component:
    """Página de analíticas del admin"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.button(
                            rx.icon("arrow-left", size=18),
                            on_click=rx.redirect("/admin"),
                            variant="ghost",
                            color="white",
                            size="2",
                        ),
                        rx.heading("Analíticas", size="7", color="white"),
                        spacing="3",
                        align="center",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Actualizar",
                        on_click=State.cargar_analytics,
                        variant="outline",
                        color_scheme="cyan",
                        size="2",
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
                rx.vstack(
                    # Loading
                    rx.cond(
                        State.cargando_analytics,
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text("Cargando analíticas...", color="#CCCCCC"),
                            spacing="3",
                        ),
                    ),
                    
                    # Error
                    rx.cond(
                        State.error_analytics != "",
                        rx.text(State.error_analytics, color="red"),
                    ),
                    
                    # Tarjetas resumen
                    rx.heading("Resumen (últimos 30 días)", size="5", color="white"),
                    rx.grid(
                        # Total visitas
                        rx.box(
                            rx.vstack(
                                rx.icon("eye", size=30, color="#00CED1"),
                                rx.heading(
                                    State.analytics_resumen.get("total_visitas", 0).to(str),
                                    size="8",
                                    color="white",
                                ),
                                rx.text("Total Visitas", color="#CCCCCC", size="2"),
                                spacing="2",
                                align="center",
                            ),
                            padding="1.5em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                        ),
                        # Visitantes únicos
                        rx.box(
                            rx.vstack(
                                rx.icon("users", size=30, color="#00CED1"),
                                rx.heading(
                                    State.analytics_resumen.get("visitantes_unicos", 0).to(str),
                                    size="8",
                                    color="white",
                                ),
                                rx.text("Visitantes Únicos", color="#CCCCCC", size="2"),
                                spacing="2",
                                align="center",
                            ),
                            padding="1.5em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                        ),
                        columns="2",
                        spacing="4",
                        width="100%",
                        max_width="500px",
                    ),
                    
                    # Páginas más visitadas
                    rx.heading("Páginas más visitadas", size="5", color="white", margin_top="1em"),
                    rx.cond(
                        State.analytics_paginas.length() > 0,
                        rx.vstack(
                            rx.foreach(
                                State.analytics_paginas,
                                lambda item: rx.hstack(
                                    rx.text(item["pagina"], color="white", size="2", width="200px"),
                                    rx.box(
                                        width=rx.cond(
                                            item["visitas"] > 0,
                                            (item["visitas"] * 5).to(str) + "px",
                                            "5px",
                                        ),
                                        height="20px",
                                        bg="#00CED1",
                                        border_radius="4px",
                                        min_width="5px",
                                        max_width="300px",
                                    ),
                                    rx.text(item["visitas"].to(str), color="#CCCCCC", size="2"),
                                    spacing="3",
                                    align="center",
                                    width="100%",
                                ),
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.text("Sin datos", color="#666", size="2"),
                    ),
                    
                    # Dispositivos y Navegadores
                    rx.grid(
                        # Dispositivos
                        rx.box(
                            rx.vstack(
                                rx.heading("Dispositivos", size="4", color="white"),
                                rx.cond(
                                    State.analytics_dispositivos.length() > 0,
                                    rx.vstack(
                                        rx.foreach(
                                            State.analytics_dispositivos,
                                            lambda item: rx.hstack(
                                                rx.text(item["dispositivo"], color="white", size="2", width="80px"),
                                                rx.text(item["total"].to(str), color="#00CED1", size="2", weight="bold"),
                                                spacing="3",
                                            ),
                                        ),
                                        spacing="2",
                                    ),
                                    rx.text("Sin datos", color="#666", size="2"),
                                ),
                                spacing="3",
                            ),
                            padding="1.5em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                        ),
                        # Navegadores
                        rx.box(
                            rx.vstack(
                                rx.heading("Navegadores", size="4", color="white"),
                                rx.cond(
                                    State.analytics_navegadores.length() > 0,
                                    rx.vstack(
                                        rx.foreach(
                                            State.analytics_navegadores,
                                            lambda item: rx.hstack(
                                                rx.text(item["navegador"], color="white", size="2", width="80px"),
                                                rx.text(item["total"].to(str), color="#00CED1", size="2", weight="bold"),
                                                spacing="3",
                                            ),
                                        ),
                                        spacing="2",
                                    ),
                                    rx.text("Sin datos", color="#666", size="2"),
                                ),
                                spacing="3",
                            ),
                            padding="1.5em",
                            border_radius="8px",
                            bg="#1a1a1a",
                            border="1px solid #333",
                        ),
                        columns="2",
                        spacing="4",
                        width="100%",
                        margin_top="1em",
                    ),
                    
                    # Visitas recientes
                    rx.heading("Visitas recientes", size="5", color="white", margin_top="1em"),
                    rx.cond(
                        State.analytics_recientes.length() > 0,
                        rx.vstack(
                            rx.foreach(
                                State.analytics_recientes,
                                lambda v: rx.hstack(
                                    rx.text(v["timestamp"], color="#666", size="1", width="160px"),
                                    rx.text(v["pagina"], color="white", size="2", width="150px"),
                                    rx.badge(v["dispositivo"], color_scheme="cyan", size="1"),
                                    rx.badge(v["navegador"], color_scheme="gray", size="1"),
                                    rx.text(v["ip"], color="#666", size="1"),
                                    spacing="3",
                                    align="center",
                                ),
                            ),
                            spacing="2",
                            width="100%",
                            overflow_x="auto",
                        ),
                        rx.text("Sin datos", color="#666", size="2"),
                    ),
                    
                    spacing="4",
                    width="100%",
                    max_width="900px",
                ),
                padding="2em",
            ),
            
            bg="#000000",
            min_height="100vh",
            on_mount=State.cargar_analytics,
        ),
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )
