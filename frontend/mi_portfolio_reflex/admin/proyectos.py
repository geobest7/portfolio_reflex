import reflex as rx
from ..states import State


def admin_proyectos() -> rx.Component:
    """Página de administración de proyectos"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Proyectos", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(
                            rx.hstack(rx.icon("arrow-left", size=20), rx.text("Volver"), spacing="2"),
                            on_click=rx.redirect("/admin"),
                            variant="outline",
                            size="2",
                        ),
                        rx.button(
                            rx.hstack(rx.icon("plus", size=20), rx.text("Nuevo Proyecto"), spacing="2"),
                            on_click=lambda: State.abrir_formulario_proyecto(0),
                            color_scheme="cyan",
                            size="2",
                        ),
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
                    State.cargando_proyectos_admin,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    rx.cond(
                        State.error_proyectos_admin != "",
                        rx.text(State.error_proyectos_admin, color="red"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Título (ES)"),
                                    rx.table.column_header_cell("Destacado"),
                                    rx.table.column_header_cell("Activo"),
                                    rx.table.column_header_cell("Orden"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.proyectos_admin,
                                    lambda proyecto: rx.table.row(
                                        rx.table.cell(proyecto.id),
                                        rx.table.cell(proyecto.titulo_es),
                                        rx.table.cell(
                                            rx.cond(
                                                proyecto.destacado,
                                                rx.badge("Sí", color_scheme="green"),
                                                rx.badge("No", color_scheme="gray"),
                                            ),
                                        ),
                                        rx.table.cell(
                                            rx.cond(
                                                proyecto.activo,
                                                rx.badge("Activo", color_scheme="blue"),
                                                rx.badge("Inactivo", color_scheme="red"),
                                            ),
                                        ),
                                        rx.table.cell(proyecto.orden),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(
                                                    rx.icon("pencil", size=16),
                                                    on_click=State.abrir_formulario_proyecto(proyecto.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                rx.button(
                                                    rx.icon("trash-2", size=16),
                                                    on_click=State.eliminar_proyecto(proyecto.id),
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="red",
                                                ),
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
                on_mount=State.cargar_proyectos_admin,
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )


def formulario_proyecto() -> rx.Component:
    """Formulario para crear/editar proyecto - versión resumida por espacio"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading(
                        rx.cond(State.modo_edicion, "Editar Proyecto", "Nuevo Proyecto"),
                        size="7",
                        color="white",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(rx.icon("x", size=20), rx.text("Cancelar"), spacing="2"),
                        on_click=State.cancelar_edicion_proyecto,
                        variant="outline",
                        size="2",
                    ),
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
                        rx.heading("Títulos", size="5", color="white", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Título (ES)", color="#CCC", size="2"),
                                rx.input(name="titulo_es", placeholder="Título en español", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_es, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (EN)", color="#CCC", size="2"),
                                rx.input(name="titulo_en", placeholder="Title in English", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_en, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (IT)", color="#CCC", size="2"),
                                rx.input(name="titulo_it", placeholder="Titolo in italiano", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_it, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Título (CA)", color="#CCC", size="2"),
                                rx.input(name="titulo_ca", placeholder="Títol en català", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.titulo_ca, ""), required=True, width="100%"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Descripciones", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Descripción (ES)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_es", placeholder="Descripción en español", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_es, ""), required=True, width="100%", rows="4"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (EN)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_en", placeholder="Description in English", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_en, ""), required=True, width="100%", rows="4"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (IT)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_it", placeholder="Descrizione in italiano", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_it, ""), required=True, width="100%", rows="4"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Descripción (CA)", color="#CCC", size="2"),
                                rx.text_area(name="descripcion_ca", placeholder="Descripció en català", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.descripcion_ca, ""), required=True, width="100%", rows="4"),
                                spacing="1", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Tecnologías (separadas por coma)", color="#CCC", size="2"),
                                rx.input(name="tecnologias", placeholder="Python,FastAPI,Reflex", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.tecnologias.join(","), ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL GitHub", color="#CCC", size="2"),
                                rx.input(name="github_url", placeholder="https://github.com/...", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.github_url, ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("URL Demo", color="#CCC", size="2"),
                                rx.input(name="demo_url", placeholder="https://...", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.demo_url, ""), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Orden", color="#CCC", size="2"),
                                rx.input(name="orden", type="number", placeholder="0", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.orden.to_string(), "0"), width="100%"),
                                spacing="1", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Destacado", color="#CCC", size="2"),
                                rx.checkbox(name="destacado", default_checked=rx.cond(State.modo_edicion, State.proyecto_editando.destacado, False)),
                                spacing="1", width="100%",
                            ),
                            columns="3", spacing="4", width="100%",
                        ),
                        rx.heading("Archivos", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Video del proyecto", color="#CCC", size="2"),
                                rx.el.input(
                                    type="file",
                                    id="_vid_file_input",
                                    accept="video/mp4,video/webm,.mp4,.webm,.mov",
                                    style={"width": "100%", "color": "#999", "padding": "0.5em", "border": "1px solid rgba(255,255,255,0.2)", "border_radius": "8px", "background": "transparent"},
                                ),
                                rx.button(
                                    rx.cond(
                                        State.subiendo_archivo,
                                        rx.hstack(rx.spinner(size="1"), rx.text("Subiendo video...", color="cyan", size="2"), spacing="2"),
                                        rx.cond(
                                            State.uploaded_video_url != "",
                                            rx.hstack(rx.icon("check", size=16, color="green"), rx.text("Video subido ✓", color="green", size="2"), spacing="2"),
                                            rx.hstack(rx.icon("upload", size=16), rx.text("Subir Video a Cloudinary"), spacing="2"),
                                        ),
                                    ),
                                    on_click=State.subir_video_directo,
                                    type="button",
                                    variant="outline",
                                    color_scheme="cyan",
                                    width="100%",
                                ),
                                rx.input(name="video_url", type="hidden", value=rx.cond(State.uploaded_video_url != "", State.uploaded_video_url, rx.cond(State.modo_edicion, State.proyecto_editando.video_url, ""))),
                                rx.text("O pega URL directamente:", color="#666", size="1"),
                                rx.input(name="video_url_manual", placeholder="https://...", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.video_url, ""), width="100%"),
                                spacing="2", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Imagen del proyecto", color="#CCC", size="2"),
                                rx.upload(
                                    rx.vstack(
                                        rx.cond(
                                            State.uploaded_imagen_url != "",
                                            rx.hstack(rx.icon("check", size=16, color="green"), rx.text("Imagen subida", color="green", size="2"), spacing="2"),
                                            rx.hstack(rx.icon("upload", size=16, color="#999"), rx.text("Suelta una imagen aquí o haz clic", color="#999", size="2"), spacing="2"),
                                        ),
                                        align="center",
                                        justify="center",
                                        padding="1.5em",
                                        border="1px dashed rgba(255,255,255,0.2)",
                                        border_radius="8px",
                                        width="100%",
                                        cursor="pointer",
                                    ),
                                    id="imagen_upload",
                                    max_files=1,
                                    max_size=10 * 1024 * 1024,
                                    no_keyboard=True,
                                    on_drop=State.upload_imagen(rx.upload_files(upload_id="imagen_upload")),
                                ),
                                rx.input(name="imagen_url", type="hidden", value=rx.cond(State.uploaded_imagen_url != "", State.uploaded_imagen_url, rx.cond(State.modo_edicion, State.proyecto_editando.imagen_url, ""))),
                                rx.text("O pega URL directamente:", color="#666", size="1"),
                                rx.input(name="imagen_url_manual", placeholder="https://...", default_value=rx.cond(State.modo_edicion, State.proyecto_editando.imagen_url, ""), width="100%"),
                                spacing="2", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.button(
                            rx.cond(State.modo_edicion, "Actualizar Proyecto", "Crear Proyecto"),
                            type="submit",
                            size="3",
                            color_scheme="cyan",
                            width="100%",
                            margin_top="2em",
                        ),
                        spacing="4", width="100%", max_width="1200px",
                    ),
                    on_submit=State.guardar_proyecto,
                    width="100%",
                ),
                padding="2em",
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )
