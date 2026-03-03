import reflex as rx
from ..states import State


def _stat_counter(stat_id: str, icon_name: str, icon_color: str, label) -> rx.Component:
    """Single stat counter with animated number"""
    return rx.vstack(
        rx.icon(icon_name, size=32, color=icon_color),
        rx.el.span(
            "0",
            id=stat_id,
            style={
                "font_size": "2.5rem",
                "font_weight": "700",
                "color": "white",
                "line_height": "1",
            },
        ),
        rx.text(label, color="#888", size="2", text_align="center"),
        spacing="2",
        align="center",
    )


def seccion_stats() -> rx.Component:
    """Sección de estadísticas con contadores animados"""
    return rx.box(
        rx.hstack(
            _stat_counter("stat-proyectos", "folder-git-2", "#00CED1", State.stats_label_proyectos),
            _stat_counter("stat-tecnologias", "cpu", "#e67e22", State.stats_label_tecnologias),
            _stat_counter("stat-certificaciones", "award", "#2ecc71", State.stats_label_certificaciones),
            _stat_counter("stat-idiomas", "languages", "#9b59b6", State.stats_label_idiomas),
            spacing="6",
            justify="center",
            wrap="wrap",
            width="100%",
            max_width="800px",
        ),
        padding="3em 2em",
        display="flex",
        justify_content="center",
        id="stats",
    )
