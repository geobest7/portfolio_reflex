import reflex as rx
from ..states import State


def admin_experiencias() -> rx.Component:
    """Página de administración de experiencias"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Experiencias", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(rx.hstack(rx.icon("arrow-left", size=20), rx.text("Volver"), spacing="2"), on_click=rx.redirect("/admin"), variant="outline", size="2"),
                        rx.button(rx.hstack(rx.icon("plus", size=20), rx.text("Nueva Experiencia"), spacing="2"), on_click=lambda: State.abrir_formulario_experiencia(0), color_scheme="cyan", size="2"),
                        spacing="3",
                    ),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            rx.box(
                rx.cond(
                    State.cargando_experiencias_admin,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    rx.cond(
                        State.error_experiencias_admin != "",
                        rx.text(State.error_experiencias_admin, color="red"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Tipo"),
                                    rx.table.column_header_cell("Empresa"),
                                    rx.table.column_header_cell("Cargo (ES)"),
                                    rx.table.column_header_cell("Fecha Inicio"),
                                    rx.table.column_header_cell("Mostrar Web"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.experiencias_admin,
                                    lambda exp: rx.table.row(
                                        rx.table.cell(exp.id),
                                        rx.table.cell(exp.tipo),
                                        rx.table.cell(exp.empresa),
                                        rx.table.cell(exp.cargo_es),
                                        rx.table.cell(exp.fecha_inicio),
                                        rx.table.cell(rx.cond(exp.mostrar_en_web, rx.badge("Sí", color_scheme="green"), rx.badge("No", color_scheme="gray"))),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(rx.icon("pencil", size=16), on_click=State.abrir_formulario_experiencia(exp.id), variant="soft", size="1", color_scheme="blue"),
                                                rx.button(rx.icon("trash-2", size=16), on_click=State.eliminar_experiencia(exp.id), variant="soft", size="1", color_scheme="red"),
                                                spacing="2",
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            variant="surface",
                            size="3",
                        ),
                    ),
                ),
                padding="2em",
                on_mount=State.cargar_experiencias_admin,
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )


def formulario_experiencia() -> rx.Component:
    """Formulario para crear/editar experiencia"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading(rx.cond(State.modo_edicion_experiencia, "Editar Experiencia", "Nueva Experiencia"), size="7", color="white"),
                    rx.spacer(),
                    rx.button(rx.hstack(rx.icon("x", size=20), rx.text("Cancelar"), spacing="2"), on_click=State.cancelar_edicion_experiencia, variant="outline", size="2"),
                    width="100%",
                    align="center",
                ),
                padding="1.5em 2em",
                bg="#1a1a1a",
                border_bottom="1px solid #333",
            ),
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading("Información General", size="5", color="white", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Tipo", color="#CCC", size="2"), rx.select(["practica", "trabajo"], name="tipo", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.tipo, "practica"), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Empresa", color="#CCC", size="2"), rx.input(name="empresa", placeholder="Nombre de la empresa", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.empresa, ""), required=True, width="100%"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Cargos", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Cargo (ES)", color="#CCC", size="2"), rx.input(name="cargo_es", placeholder="Cargo en español", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_es, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Cargo (EN)", color="#CCC", size="2"), rx.input(name="cargo_en", placeholder="Position in English", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_en, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Cargo (IT)", color="#CCC", size="2"), rx.input(name="cargo_it", placeholder="Posizione in italiano", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_it, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Cargo (CA)", color="#CCC", size="2"), rx.input(name="cargo_ca", placeholder="Càrrec en català", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.cargo_ca, ""), required=True, width="100%"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Descripciones (opcional)", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Descripción (ES)", color="#CCC", size="2"), rx.text_area(name="descripcion_es", placeholder="Descripción en español", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_es, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (EN)", color="#CCC", size="2"), rx.text_area(name="descripcion_en", placeholder="Description in English", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_en, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (IT)", color="#CCC", size="2"), rx.text_area(name="descripcion_it", placeholder="Descrizione in italiano", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_it, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (CA)", color="#CCC", size="2"), rx.text_area(name="descripcion_ca", placeholder="Descripció en català", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.descripcion_ca, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Fecha Inicio", color="#CCC", size="2"), rx.input(name="fecha_inicio", type="date", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.fecha_inicio, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Fecha Fin (opcional)", color="#CCC", size="2"), rx.input(name="fecha_fin", type="date", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.fecha_fin, ""), width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Tecnologías (separadas por coma)", color="#CCC", size="2"), rx.input(name="tecnologias", placeholder="Python,FastAPI,React", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.tecnologias.join(","), ""), width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("URL Video (YouTube)", color="#CCC", size="2"), rx.input(name="video_url", placeholder="https://www.youtube.com/watch?v=...", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.video_url, ""), width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Orden", color="#CCC", size="2"), rx.input(name="orden", type="number", placeholder="0", default_value=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.orden.to_string(), "0"), width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Trabajo Actual", color="#CCC", size="2"), rx.checkbox(name="actual", default_checked=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.actual, False)), spacing="1", width="100%"),
                            rx.vstack(rx.text("Mostrar en Web", color="#CCC", size="2"), rx.checkbox(name="mostrar_en_web", default_checked=rx.cond(State.modo_edicion_experiencia, State.experiencia_editando.mostrar_en_web, False)), spacing="1", width="100%"),
                            columns="3", spacing="4", width="100%",
                        ),
                        rx.button(rx.cond(State.modo_edicion_experiencia, "Actualizar Experiencia", "Crear Experiencia"), type="submit", size="3", color_scheme="cyan", width="100%", margin_top="2em"),
                        spacing="4", width="100%", max_width="1200px",
                    ),
                    on_submit=State.guardar_experiencia,
                    width="100%",
                ),
                padding="2em",
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )
