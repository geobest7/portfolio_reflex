import reflex as rx
from ..states import State


def admin_cursos() -> rx.Component:
    """Página de administración de cursos"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading("Gestión de Cursos", size="7", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.button(rx.hstack(rx.icon("arrow-left", size=20), rx.text("Volver"), spacing="2"), on_click=rx.redirect("/admin"), variant="outline", size="2"),
                        rx.button(rx.hstack(rx.icon("plus", size=20), rx.text("Nuevo Curso"), spacing="2"), on_click=lambda: State.abrir_formulario_curso(0), color_scheme="cyan", size="2"),
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
                    State.cargando_cursos_admin,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    rx.cond(
                        State.error_cursos_admin != "",
                        rx.text(State.error_cursos_admin, color="red"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Título (ES)"),
                                    rx.table.column_header_cell("Institución (ES)"),
                                    rx.table.column_header_cell("Fecha Inicio"),
                                    rx.table.column_header_cell("Activo"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    State.cursos_admin,
                                    lambda curso: rx.table.row(
                                        rx.table.cell(curso.id),
                                        rx.table.cell(curso.titulo_es),
                                        rx.table.cell(curso.institucion_es),
                                        rx.table.cell(curso.fecha_inicio),
                                        rx.table.cell(rx.cond(curso.activo, rx.badge("Activo", color_scheme="blue"), rx.badge("Inactivo", color_scheme="red"))),
                                        rx.table.cell(
                                            rx.hstack(
                                                rx.button(rx.icon("pencil", size=16), on_click=State.abrir_formulario_curso(curso.id), variant="soft", size="1", color_scheme="blue"),
                                                rx.button(rx.icon("trash-2", size=16), on_click=State.eliminar_curso(curso.id), variant="soft", size="1", color_scheme="red"),
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
                on_mount=State.cargar_cursos_admin,
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )


def formulario_curso() -> rx.Component:
    """Formulario para crear/editar curso"""
    return rx.cond(
        State.esta_autenticado,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.heading(rx.cond(State.modo_edicion_curso, "Editar Curso", "Nuevo Curso"), size="7", color="white"),
                    rx.spacer(),
                    rx.button(rx.hstack(rx.icon("x", size=20), rx.text("Cancelar"), spacing="2"), on_click=State.cancelar_edicion_curso, variant="outline", size="2"),
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
                        rx.heading("Tipo", size="5", color="white", margin_bottom="0.5em"),
                        rx.select(["diploma", "curso", "certificacion"], name="tipo", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.tipo, "curso"), required=True, width="300px"),
                        rx.heading("Títulos", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Título (ES)", color="#CCC", size="2"), rx.input(name="titulo_es", placeholder="Título en español", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_es, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Título (EN)", color="#CCC", size="2"), rx.input(name="titulo_en", placeholder="Title in English", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_en, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Título (IT)", color="#CCC", size="2"), rx.input(name="titulo_it", placeholder="Titolo in italiano", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_it, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Título (CA)", color="#CCC", size="2"), rx.input(name="titulo_ca", placeholder="Títol en català", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.titulo_ca, ""), required=True, width="100%"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Instituciones", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Institución (ES)", color="#CCC", size="2"), rx.input(name="institucion_es", placeholder="Institución en español", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_es, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Institución (EN)", color="#CCC", size="2"), rx.input(name="institucion_en", placeholder="Institution in English", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_en, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Institución (IT)", color="#CCC", size="2"), rx.input(name="institucion_it", placeholder="Istituzione in italiano", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_it, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Institución (CA)", color="#CCC", size="2"), rx.input(name="institucion_ca", placeholder="Institució en català", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.institucion_ca, ""), required=True, width="100%"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Descripciones (opcional)", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Descripción (ES)", color="#CCC", size="2"), rx.text_area(name="descripcion_es", placeholder="Descripción en español", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.descripcion_es, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (EN)", color="#CCC", size="2"), rx.text_area(name="descripcion_en", placeholder="Description in English", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.descripcion_en, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (IT)", color="#CCC", size="2"), rx.text_area(name="descripcion_it", placeholder="Descrizione in italiano", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.descripcion_it, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Descripción (CA)", color="#CCC", size="2"), rx.text_area(name="descripcion_ca", placeholder="Descripció en català", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.descripcion_ca, ""), width="100%", rows="3"), spacing="1", width="100%"),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.heading("Detalles", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(rx.text("Fecha Inicio", color="#CCC", size="2"), rx.input(name="fecha_inicio", type="date", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.fecha_inicio, ""), required=True, width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Fecha Fin (opcional)", color="#CCC", size="2"), rx.input(name="fecha_fin", type="date", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.fecha_fin, ""), width="100%"), spacing="1", width="100%"),
                            rx.vstack(rx.text("Orden", color="#CCC", size="2"), rx.input(name="orden", type="number", placeholder="0", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.orden.to_string(), "0"), width="100%"), spacing="1", width="100%"),
                            columns="3", spacing="4", width="100%",
                        ),
                        rx.heading("Archivos", size="5", color="white", margin_top="1em", margin_bottom="0.5em"),
                        rx.grid(
                            rx.vstack(
                                rx.text("Diploma PDF", color="#CCC", size="2"),
                                rx.upload(
                                    rx.vstack(
                                        rx.cond(
                                            State.uploaded_diploma_url != "",
                                            rx.hstack(rx.icon("check", size=16, color="green"), rx.text("Diploma subido", color="green", size="2"), spacing="2"),
                                            rx.hstack(rx.icon("upload", size=16, color="#999"), rx.text("Arrastra o haz clic para subir PDF", color="#999", size="2"), spacing="2"),
                                        ),
                                        align="center",
                                        justify="center",
                                        padding="1em",
                                        border="1px dashed rgba(255,255,255,0.2)",
                                        border_radius="8px",
                                        width="100%",
                                        cursor="pointer",
                                    ),
                                    id="diploma_upload",
                                    accept={".pdf": ["application/pdf"]},
                                    max_files=1,
                                    no_keyboard=True,
                                ),
                                rx.button(
                                    rx.cond(State.subiendo_archivo, rx.spinner(size="1"), rx.text("Subir Diploma")),
                                    on_click=State.upload_diploma(rx.upload_files(upload_id="diploma_upload")),
                                    size="1",
                                    variant="outline",
                                    width="100%",
                                    disabled=State.subiendo_archivo,
                                ),
                                rx.input(name="diploma_pdf", type="hidden", value=rx.cond(State.uploaded_diploma_url != "", State.uploaded_diploma_url, rx.cond(State.modo_edicion_curso, State.curso_editando.diploma_pdf, ""))),
                                rx.text("O pega URL directamente:", color="#666", size="1"),
                                rx.input(name="diploma_pdf_manual", placeholder="https://...", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.diploma_pdf, ""), width="100%"),
                                spacing="2", width="100%",
                            ),
                            rx.vstack(
                                rx.text("Certificado", color="#CCC", size="2"),
                                rx.upload(
                                    rx.vstack(
                                        rx.cond(
                                            State.uploaded_certificado_url != "",
                                            rx.hstack(rx.icon("check", size=16, color="green"), rx.text("Certificado subido", color="green", size="2"), spacing="2"),
                                            rx.hstack(rx.icon("upload", size=16, color="#999"), rx.text("Arrastra o haz clic para subir", color="#999", size="2"), spacing="2"),
                                        ),
                                        align="center",
                                        justify="center",
                                        padding="1em",
                                        border="1px dashed rgba(255,255,255,0.2)",
                                        border_radius="8px",
                                        width="100%",
                                        cursor="pointer",
                                    ),
                                    id="cert_upload",
                                    accept={".pdf": ["application/pdf"], ".jpg": ["image/jpeg"], ".png": ["image/png"]},
                                    max_files=1,
                                    no_keyboard=True,
                                ),
                                rx.button(
                                    rx.cond(State.subiendo_archivo, rx.spinner(size="1"), rx.text("Subir Certificado")),
                                    on_click=State.upload_certificado(rx.upload_files(upload_id="cert_upload")),
                                    size="1",
                                    variant="outline",
                                    width="100%",
                                    disabled=State.subiendo_archivo,
                                ),
                                rx.input(name="certificado_url", type="hidden", value=rx.cond(State.uploaded_certificado_url != "", State.uploaded_certificado_url, rx.cond(State.modo_edicion_curso, State.curso_editando.certificado_url, ""))),
                                rx.text("O pega URL directamente:", color="#666", size="1"),
                                rx.input(name="certificado_url_manual", placeholder="https://...", default_value=rx.cond(State.modo_edicion_curso, State.curso_editando.certificado_url, ""), width="100%"),
                                spacing="2", width="100%",
                            ),
                            columns="2", spacing="4", width="100%",
                        ),
                        rx.button(rx.cond(State.modo_edicion_curso, "Actualizar Curso", "Crear Curso"), type="submit", size="3", color_scheme="cyan", width="100%", margin_top="2em"),
                        spacing="4", width="100%", max_width="1200px",
                    ),
                    on_submit=State.guardar_curso,
                    width="100%",
                ),
                padding="2em",
            ),
            bg="#000000",
            min_height="100vh",
        ),
        rx.fragment(rx.script("window.location.href = '/login'")),
    )
