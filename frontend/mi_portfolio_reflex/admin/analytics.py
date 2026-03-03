import reflex as rx
from ..states import State


def _card(title: str, icon_name: str, icon_color: str, content: rx.Component) -> rx.Component:
    """Card genérica con título e icono"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(icon_name, size=18, color=icon_color),
                rx.text(title, color="white", size="3", weight="bold"),
                spacing="2",
                align="center",
            ),
            content,
            spacing="3",
            width="100%",
        ),
        padding="1.2em",
        border_radius="10px",
        bg="#111111",
        border="1px solid #222",
        width="100%",
    )


def _stat_card(icon_name: str, icon_color: str, value, label: str, sublabel: str) -> rx.Component:
    """Card de estadística grande"""
    return rx.box(
        rx.vstack(
            rx.icon(icon_name, size=28, color=icon_color),
            rx.heading(value, size="8", color="white"),
            rx.text(label, color="#888", size="2"),
            rx.text(sublabel, color="#555", size="1"),
            spacing="1",
            align="center",
        ),
        padding="1.5em",
        border_radius="10px",
        bg="#111111",
        border="1px solid #222",
    )


def _data_row(label, value, color: str = "white") -> rx.Component:
    """Fila label → valor alineado"""
    return rx.hstack(
        rx.text(label, color="#AAA", size="2"),
        rx.spacer(),
        rx.text(value, color=color, size="2", weight="bold"),
        spacing="2",
        align="center",
        width="100%",
    )


def admin_analytics() -> rx.Component:
    """Página de analíticas del admin con gráficos"""
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
                    
                    # ===== RESUMEN (4 stat cards) =====
                    rx.grid(
                        _stat_card(
                            "eye", "#00CED1",
                            State.analytics_total_visitas,
                            "Visitas totales", "Últimos 30 días",
                        ),
                        _stat_card(
                            "users", "#9b59b6",
                            State.analytics_visitantes_unicos,
                            "Visitantes únicos", "Por IP anonimizada",
                        ),
                        _stat_card(
                            "trending-up", "#2ecc71",
                            State.analytics_visitas_hoy,
                            "Visitas hoy", "Tiempo real",
                        ),
                        _stat_card(
                            "calendar-days", "#e67e22",
                            State.analytics_media_diaria,
                            "Media diaria", "Últimos 30 días",
                        ),
                        columns=rx.breakpoints(initial="2", md="4"),
                        spacing="3",
                        width="100%",
                    ),
                    
                    # ===== GRÁFICO: Visitas por día (Area Chart) =====
                    rx.cond(
                        State.analytics_por_dia.length() > 0,
                        _card(
                            "Visitas por día", "trending-up", "#00CED1",
                            rx.recharts.area_chart(
                                rx.recharts.area(
                                    data_key="visitas",
                                    stroke="#00CED1",
                                    fill="#00CED1",
                                    fill_opacity=0.15,
                                    type_="monotone",
                                ),
                                rx.recharts.x_axis(
                                    data_key="label",
                                    tick={"fill": "#888", "fontSize": 11},
                                    stroke="#333",
                                ),
                                rx.recharts.y_axis(
                                    tick={"fill": "#888", "fontSize": 11},
                                    stroke="#333",
                                    width=35,
                                ),
                                rx.recharts.cartesian_grid(stroke_dasharray="3 3", stroke="#222"),
                                rx.recharts.tooltip(
                                    content_style={"backgroundColor": "#1a1a1a", "border": "1px solid #333", "borderRadius": "8px"},
                                    label_style={"color": "#aaa"},
                                ),
                                data=State.analytics_por_dia_chart,
                                width="100%",
                                height=250,
                            ),
                        ),
                    ),
                    
                    # ===== FILA: Dispositivos (Pie) + Navegadores (Pie) =====
                    rx.grid(
                        _card(
                            "Dispositivos", "monitor-smartphone", "#e67e22",
                            rx.cond(
                                State.analytics_dispositivos.length() > 0,
                                rx.recharts.pie_chart(
                                    rx.recharts.pie(
                                        data=State.analytics_dispositivos_chart,
                                        data_key="value",
                                        name_key="name",
                                        cx="50%",
                                        cy="50%",
                                        outer_radius=70,
                                        label=True,
                                        fill="#e67e22",
                                    ),
                                    rx.recharts.tooltip(
                                        content_style={"backgroundColor": "#1a1a1a", "border": "1px solid #333", "borderRadius": "8px"},
                                    ),
                                    rx.recharts.legend(
                                        wrapper_style={"color": "#aaa", "fontSize": "12px"},
                                    ),
                                    width="100%",
                                    height=220,
                                ),
                                rx.text("Sin datos aún", color="#555", size="2"),
                            ),
                        ),
                        _card(
                            "Navegadores", "globe", "#9b59b6",
                            rx.cond(
                                State.analytics_navegadores.length() > 0,
                                rx.recharts.pie_chart(
                                    rx.recharts.pie(
                                        data=State.analytics_navegadores_chart,
                                        data_key="value",
                                        name_key="name",
                                        cx="50%",
                                        cy="50%",
                                        outer_radius=70,
                                        label=True,
                                        fill="#9b59b6",
                                    ),
                                    rx.recharts.tooltip(
                                        content_style={"backgroundColor": "#1a1a1a", "border": "1px solid #333", "borderRadius": "8px"},
                                    ),
                                    rx.recharts.legend(
                                        wrapper_style={"color": "#aaa", "fontSize": "12px"},
                                    ),
                                    width="100%",
                                    height=220,
                                ),
                                rx.text("Sin datos aún", color="#555", size="2"),
                            ),
                        ),
                        columns=rx.breakpoints(initial="1", md="2"),
                        spacing="3",
                        width="100%",
                    ),
                    
                    # ===== FILA: SO (Bar) + Páginas (Bar) =====
                    rx.grid(
                        _card(
                            "Sistemas Operativos", "cpu", "#2ecc71",
                            rx.cond(
                                State.analytics_plataformas.length() > 0,
                                rx.recharts.bar_chart(
                                    rx.recharts.bar(
                                        data_key="value",
                                        fill="#2ecc71",
                                        radius=[4, 4, 0, 0],
                                    ),
                                    rx.recharts.x_axis(
                                        data_key="name",
                                        tick={"fill": "#888", "fontSize": 11},
                                        stroke="#333",
                                    ),
                                    rx.recharts.y_axis(
                                        tick={"fill": "#888", "fontSize": 11},
                                        stroke="#333",
                                        width=30,
                                    ),
                                    rx.recharts.tooltip(
                                        content_style={"backgroundColor": "#1a1a1a", "border": "1px solid #333", "borderRadius": "8px"},
                                    ),
                                    data=State.analytics_plataformas_chart,
                                    width="100%",
                                    height=200,
                                ),
                                rx.text("Sin datos aún", color="#555", size="2"),
                            ),
                        ),
                        _card(
                            "Páginas visitadas", "file-text", "#00CED1",
                            rx.cond(
                                State.analytics_paginas.length() > 0,
                                rx.recharts.bar_chart(
                                    rx.recharts.bar(
                                        data_key="value",
                                        fill="#00CED1",
                                        radius=[4, 4, 0, 0],
                                    ),
                                    rx.recharts.x_axis(
                                        data_key="name",
                                        tick={"fill": "#888", "fontSize": 11},
                                        stroke="#333",
                                    ),
                                    rx.recharts.y_axis(
                                        tick={"fill": "#888", "fontSize": 11},
                                        stroke="#333",
                                        width=30,
                                    ),
                                    rx.recharts.tooltip(
                                        content_style={"backgroundColor": "#1a1a1a", "border": "1px solid #333", "borderRadius": "8px"},
                                    ),
                                    data=State.analytics_paginas_chart,
                                    width="100%",
                                    height=200,
                                ),
                                rx.text("Sin datos aún", color="#555", size="2"),
                            ),
                        ),
                        columns=rx.breakpoints(initial="1", md="2"),
                        spacing="3",
                        width="100%",
                    ),
                    
                    # ===== REFERRERS =====
                    rx.cond(
                        State.analytics_referrers.length() > 0,
                        _card(
                            "Origen del tráfico", "external-link", "#3498db",
                            rx.vstack(
                                rx.foreach(
                                    State.analytics_referrers,
                                    lambda item: rx.hstack(
                                        rx.text(
                                            item["referrer"],
                                            color="#AAA",
                                            size="2",
                                            overflow="hidden",
                                            text_overflow="ellipsis",
                                            white_space="nowrap",
                                        ),
                                        rx.spacer(),
                                        rx.badge(item["total"], color_scheme="blue", variant="solid", size="1"),
                                        spacing="2",
                                        align="center",
                                        width="100%",
                                    ),
                                ),
                                spacing="2",
                                width="100%",
                            ),
                        ),
                    ),
                    
                    # ===== VISITAS RECIENTES (tabla) =====
                    rx.cond(
                        State.analytics_recientes.length() > 0,
                        _card(
                            "Últimas visitas", "clock", "#00CED1",
                            rx.vstack(
                                # Header
                                rx.hstack(
                                    rx.text("Fecha", color="#555", size="1", weight="bold", min_width="75px"),
                                    rx.text("Pág.", color="#555", size="1", weight="bold", width="100%"),
                                    rx.text("Disp.", color="#555", size="1", weight="bold", min_width="65px"),
                                    rx.text("Nav.", color="#555", size="1", weight="bold", min_width="65px"),
                                    rx.text("SO", color="#555", size="1", weight="bold", min_width="65px"),
                                    rx.text("IP", color="#555", size="1", weight="bold", min_width="100px"),
                                    spacing="2",
                                    width="100%",
                                    padding_bottom="0.4em",
                                    border_bottom="1px solid #222",
                                ),
                                # Filas
                                rx.foreach(
                                    State.analytics_recientes,
                                    lambda v: rx.hstack(
                                        rx.vstack(
                                            rx.text(v["timestamp"][5:10], color="#AAA", size="1"),
                                            rx.text(v["timestamp"][11:16], color="#555", size="1"),
                                            spacing="0",
                                            min_width="75px",
                                        ),
                                        rx.text(
                                            v["pagina"], color="white", size="1",
                                            width="100%",
                                            overflow="hidden",
                                            text_overflow="ellipsis",
                                            white_space="nowrap",
                                        ),
                                        rx.badge(
                                            v["dispositivo"],
                                            color_scheme=rx.cond(
                                                v["dispositivo"] == "movil", "orange",
                                                rx.cond(v["dispositivo"] == "tablet", "purple", "cyan"),
                                            ),
                                            variant="soft", size="1", min_width="65px",
                                        ),
                                        rx.badge(v["navegador"], color_scheme="gray", variant="soft", size="1", min_width="65px"),
                                        rx.text(v["plataforma"], color="#666", size="1", min_width="65px"),
                                        rx.text(v["ip"], color="#444", size="1", min_width="100px"),
                                        spacing="2",
                                        align="center",
                                        width="100%",
                                        padding_y="0.3em",
                                        border_bottom="1px solid #1a1a1a",
                                    ),
                                ),
                                spacing="0",
                                width="100%",
                            ),
                        ),
                    ),
                    
                    spacing="3",
                    width="100%",
                    max_width="1100px",
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
