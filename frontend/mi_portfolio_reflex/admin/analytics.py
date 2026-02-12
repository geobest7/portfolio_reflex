import reflex as rx
from ..states import State


def _stat_card(icon_name: str, value, label: str, color: str = "#00CED1") -> rx.Component:
    """Tarjeta de estadística individual"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon_name, size=22, color=color),
                    padding="0.6em",
                    border_radius="8px",
                    bg=f"rgba(0, 206, 209, 0.1)",
                ),
                rx.spacer(),
                spacing="3",
                width="100%",
                align="center",
            ),
            rx.heading(value, size="7", color="white", margin_top="0.3em"),
            rx.text(label, color="#888", size="2"),
            spacing="1",
            align="start",
            width="100%",
        ),
        padding="1.2em",
        border_radius="10px",
        bg="#111111",
        border="1px solid #222",
        width="100%",
    )


def _section_title(title: str, icon_name: str) -> rx.Component:
    """Título de sección con icono"""
    return rx.hstack(
        rx.icon(icon_name, size=20, color="#00CED1"),
        rx.heading(title, size="5", color="white"),
        spacing="2",
        align="center",
        margin_top="1.5em",
        margin_bottom="0.5em",
    )


def _bar_row(label, count, max_val, color: str = "#00CED1") -> rx.Component:
    """Fila con barra de progreso visual"""
    return rx.hstack(
        rx.text(label, color="#CCC", size="2", min_width="100px"),
        rx.box(
            rx.box(
                width=rx.cond(
                    max_val > 0,
                    (count * 100 / max_val).to(str) + "%",
                    "0%",
                ),
                height="100%",
                bg=color,
                border_radius="4px",
            ),
            width="100%",
            height="8px",
            bg="#222",
            border_radius="4px",
            overflow="hidden",
        ),
        rx.text(count.to(str), color="white", size="2", weight="bold", min_width="40px", text_align="right"),
        spacing="3",
        align="center",
        width="100%",
    )


def _format_timestamp(ts: str) -> rx.Component:
    """Formato legible de timestamp"""
    return rx.vstack(
        rx.text(ts[0:10], color="#CCC", size="1"),
        rx.text(ts[11:16], color="#666", size="1"),
        spacing="0",
        align="start",
    )


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
                        rx.icon("bar-chart-3", size=24, color="#00CED1"),
                        rx.heading("Analíticas", size="7", color="white"),
                        spacing="3",
                        align="center",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(
                            rx.icon("download", size=16),
                            "Excel",
                            on_click=State.descargar_excel_analytics,
                            variant="solid",
                            color_scheme="green",
                            size="2",
                        ),
                        rx.button(
                            rx.icon("refresh-cw", size=16),
                            "Actualizar",
                            on_click=State.cargar_analytics,
                            variant="outline",
                            color_scheme="cyan",
                            size="2",
                        ),
                        spacing="2",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#0a0a0a",
                border_bottom="1px solid #222",
            ),
            
            # Contenido
            rx.box(
                rx.vstack(
                    # Loading
                    rx.cond(
                        State.cargando_analytics,
                        rx.center(
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Cargando analíticas...", color="#888"),
                                spacing="3",
                            ),
                            padding="2em",
                        ),
                    ),
                    
                    # Error
                    rx.cond(
                        State.error_analytics != "",
                        rx.box(
                            rx.text(State.error_analytics, color="#ff6b6b"),
                            padding="1em",
                            bg="#1a0000",
                            border="1px solid #ff6b6b",
                            border_radius="8px",
                        ),
                    ),
                    
                    # ===== RESUMEN =====
                    _section_title("Resumen (últimos 30 días)", "activity"),
                    rx.grid(
                        _stat_card(
                            "eye",
                            State.analytics_resumen.get("total_visitas", 0).to(str),
                            "Total Visitas",
                        ),
                        _stat_card(
                            "users",
                            State.analytics_resumen.get("visitantes_unicos", 0).to(str),
                            "Visitantes Únicos",
                            "#9b59b6",
                        ),
                        columns="2",
                        spacing="3",
                        width="100%",
                    ),
                    
                    # ===== VISITAS POR DÍA =====
                    _section_title("Visitas por día", "calendar"),
                    rx.cond(
                        State.analytics_por_dia.length() > 0,
                        rx.box(
                            rx.vstack(
                                rx.foreach(
                                    State.analytics_por_dia,
                                    lambda item: rx.hstack(
                                        rx.text(item["fecha"], color="#888", size="1", min_width="85px"),
                                        rx.box(
                                            rx.box(
                                                width=item["visitas"].to(str) + "0%",
                                                max_width="100%",
                                                height="100%",
                                                bg="linear-gradient(90deg, #00CED1, #0099aa)",
                                                border_radius="3px",
                                            ),
                                            width="100%",
                                            height="20px",
                                            bg="#1a1a1a",
                                            border_radius="3px",
                                            overflow="hidden",
                                        ),
                                        rx.text(
                                            item["visitas"].to(str),
                                            color="white",
                                            size="1",
                                            weight="bold",
                                            min_width="30px",
                                            text_align="right",
                                        ),
                                        spacing="2",
                                        align="center",
                                        width="100%",
                                    ),
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            padding="1.2em",
                            border_radius="10px",
                            bg="#111111",
                            border="1px solid #222",
                            width="100%",
                        ),
                        rx.text("Sin datos", color="#666", size="2"),
                    ),
                    
                    # ===== PÁGINAS + DISPOSITIVOS + NAVEGADORES =====
                    rx.grid(
                        # Páginas más visitadas
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("file-text", size=18, color="#00CED1"),
                                    rx.text("Páginas más visitadas", color="white", size="3", weight="bold"),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.cond(
                                    State.analytics_paginas.length() > 0,
                                    rx.vstack(
                                        rx.foreach(
                                            State.analytics_paginas,
                                            lambda item: rx.hstack(
                                                rx.text(
                                                    item["pagina"],
                                                    color="#CCC",
                                                    size="2",
                                                    min_width="120px",
                                                    overflow="hidden",
                                                    text_overflow="ellipsis",
                                                    white_space="nowrap",
                                                ),
                                                rx.spacer(),
                                                rx.badge(
                                                    item["visitas"].to(str),
                                                    color_scheme="cyan",
                                                    variant="solid",
                                                    size="1",
                                                ),
                                                spacing="2",
                                                align="center",
                                                width="100%",
                                            ),
                                        ),
                                        spacing="2",
                                        width="100%",
                                    ),
                                    rx.text("Sin datos", color="#666", size="2"),
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            padding="1.2em",
                            border_radius="10px",
                            bg="#111111",
                            border="1px solid #222",
                        ),
                        # Dispositivos
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("monitor-smartphone", size=18, color="#e67e22"),
                                    rx.text("Dispositivos", color="white", size="3", weight="bold"),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.cond(
                                    State.analytics_dispositivos.length() > 0,
                                    rx.vstack(
                                        rx.foreach(
                                            State.analytics_dispositivos,
                                            lambda item: rx.hstack(
                                                rx.icon(
                                                    rx.cond(
                                                        item["dispositivo"] == "mobile",
                                                        "smartphone",
                                                        rx.cond(
                                                            item["dispositivo"] == "tablet",
                                                            "tablet",
                                                            "monitor",
                                                        ),
                                                    ),
                                                    size=16,
                                                    color="#e67e22",
                                                ),
                                                rx.text(item["dispositivo"], color="#CCC", size="2"),
                                                rx.spacer(),
                                                rx.text(item["total"].to(str), color="white", size="2", weight="bold"),
                                                spacing="2",
                                                align="center",
                                                width="100%",
                                            ),
                                        ),
                                        spacing="2",
                                        width="100%",
                                    ),
                                    rx.text("Sin datos", color="#666", size="2"),
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            padding="1.2em",
                            border_radius="10px",
                            bg="#111111",
                            border="1px solid #222",
                        ),
                        # Navegadores
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("globe", size=18, color="#9b59b6"),
                                    rx.text("Navegadores", color="white", size="3", weight="bold"),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.cond(
                                    State.analytics_navegadores.length() > 0,
                                    rx.vstack(
                                        rx.foreach(
                                            State.analytics_navegadores,
                                            lambda item: rx.hstack(
                                                rx.text(item["navegador"], color="#CCC", size="2"),
                                                rx.spacer(),
                                                rx.text(item["total"].to(str), color="white", size="2", weight="bold"),
                                                spacing="2",
                                                align="center",
                                                width="100%",
                                            ),
                                        ),
                                        spacing="2",
                                        width="100%",
                                    ),
                                    rx.text("Sin datos", color="#666", size="2"),
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            padding="1.2em",
                            border_radius="10px",
                            bg="#111111",
                            border="1px solid #222",
                        ),
                        columns="3",
                        spacing="3",
                        width="100%",
                    ),
                    
                    # ===== VISITAS RECIENTES =====
                    _section_title("Visitas recientes", "clock"),
                    rx.cond(
                        State.analytics_recientes.length() > 0,
                        rx.box(
                            rx.vstack(
                                # Header de tabla
                                rx.hstack(
                                    rx.text("Fecha", color="#666", size="1", weight="bold", min_width="75px"),
                                    rx.text("Página", color="#666", size="1", weight="bold", width="100%"),
                                    rx.text("Dispositivo", color="#666", size="1", weight="bold", min_width="80px"),
                                    rx.text("Navegador", color="#666", size="1", weight="bold", min_width="80px"),
                                    rx.text("IP", color="#666", size="1", weight="bold", min_width="110px"),
                                    spacing="3",
                                    width="100%",
                                    padding_bottom="0.5em",
                                    border_bottom="1px solid #222",
                                ),
                                # Filas
                                rx.foreach(
                                    State.analytics_recientes,
                                    lambda v: rx.hstack(
                                        rx.vstack(
                                            rx.text(v["timestamp"][0:10], color="#AAA", size="1"),
                                            rx.text(v["timestamp"][11:16], color="#666", size="1"),
                                            spacing="0",
                                            min_width="75px",
                                        ),
                                        rx.text(
                                            v["pagina"],
                                            color="white",
                                            size="1",
                                            width="100%",
                                            overflow="hidden",
                                            text_overflow="ellipsis",
                                            white_space="nowrap",
                                        ),
                                        rx.badge(
                                            v["dispositivo"],
                                            color_scheme=rx.cond(
                                                v["dispositivo"] == "mobile",
                                                "orange",
                                                rx.cond(
                                                    v["dispositivo"] == "tablet",
                                                    "purple",
                                                    "cyan",
                                                ),
                                            ),
                                            variant="soft",
                                            size="1",
                                            min_width="80px",
                                        ),
                                        rx.badge(
                                            v["navegador"],
                                            color_scheme="gray",
                                            variant="soft",
                                            size="1",
                                            min_width="80px",
                                        ),
                                        rx.text(v["ip"], color="#555", size="1", min_width="110px"),
                                        spacing="3",
                                        align="center",
                                        width="100%",
                                        padding_y="0.4em",
                                        border_bottom="1px solid #1a1a1a",
                                        _hover={"bg": "#0a0a0a"},
                                    ),
                                ),
                                spacing="0",
                                width="100%",
                            ),
                            padding="1.2em",
                            border_radius="10px",
                            bg="#111111",
                            border="1px solid #222",
                            width="100%",
                            overflow_x="auto",
                        ),
                        rx.text("Sin datos", color="#666", size="2"),
                    ),
                    
                    spacing="3",
                    width="100%",
                    max_width="1000px",
                ),
                padding="1.5em",
            ),
            
            bg="#000000",
            min_height="100vh",
            on_mount=State.cargar_analytics,
        ),
        rx.fragment(
            rx.script("window.location.href = '/login'"),
        ),
    )
