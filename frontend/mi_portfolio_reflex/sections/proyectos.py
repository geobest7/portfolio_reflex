import reflex as rx
from ..states import State
from ..components.skeletons import skeleton_proyecto


def seccion_proyectos() -> rx.Component:
    """Seccion Proyectos con datos dinamicos desde la API"""
    return rx.box(
        rx.vstack(
            rx.heading(State.proyectos_titulo, size="8", color="white", text_align="center", width="100%"),
            
            rx.cond(
                State.cargando_proyectos,
                rx.box(
                    rx.hstack(
                        skeleton_proyecto(),
                        skeleton_proyecto(),
                        skeleton_proyecto(),
                        spacing="3",
                        wrap="wrap",
                    ),
                    class_name="proyectos-grid",
                    width="100%",
                ),
            ),
            
            rx.cond(
                State.error_proyectos != "",
                rx.text(State.error_proyectos, color="red"),
            ),
            
            rx.box(
                rx.foreach(
                    State.proyectos,
                    lambda proyecto: rx.box(
                        rx.vstack(
                            rx.heading(
                                rx.cond(
                                    State.idioma == "es",
                                    proyecto.titulo_es,
                                    rx.cond(
                                        State.idioma == "en",
                                        proyecto.titulo_en,
                                        rx.cond(
                                            State.idioma == "it",
                                            proyecto.titulo_it,
                                            proyecto.titulo_ca
                                        )
                                    )
                                ),
                                size="5",
                                color="#E040FB",
                            ),
                            rx.text(
                                rx.cond(
                                    State.idioma == "es",
                                    proyecto.descripcion_es,
                                    rx.cond(
                                        State.idioma == "en",
                                        proyecto.descripcion_en,
                                        rx.cond(
                                            State.idioma == "it",
                                            proyecto.descripcion_it,
                                            proyecto.descripcion_ca
                                        )
                                    )
                                ),
                                color="#CCCCCC",
                                size="2",
                            ),
                            
                            # Imagen del proyecto
                            rx.cond(
                                proyecto.imagen_url != "",
                                rx.image(
                                    src=proyecto.imagen_url,
                                    width="100%",
                                    max_height="300px",
                                    object_fit="cover",
                                    border_radius="8px",
                                    margin_top="0.5em",
                                    loading="lazy",
                                ),
                            ),
                            
                            # Video del proyecto (Cloudinary) con poster auto-generado
                            rx.cond(
                                proyecto.video_url != "",
                                rx.box(
                                    rx.el.video(
                                        rx.el.source(src=proyecto.video_url, type="video/mp4"),
                                        controls=True,
                                        preload="none",
                                        poster=proyecto.video_url.replace("/video/upload/", "/video/upload/so_0,w_600,q_auto/").replace(".mp4", ".jpg").replace(".webm", ".jpg").replace(".mov", ".jpg"),
                                        width="100%",
                                        style={"border_radius": "8px", "max_height": "400px", "background": "#111"},
                                    ),
                                    width="100%",
                                    margin_top="0.5em",
                                ),
                            ),
                            
                            rx.hstack(
                                rx.foreach(
                                    proyecto.tecnologias,
                                    lambda tech: rx.badge(tech, color_scheme="gray"),
                                ),
                                wrap="wrap",
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.cond(
                                    proyecto.github_url != "",
                                    rx.link(
                                        rx.button("Ver codigo", variant="outline"),
                                        href=proyecto.github_url,
                                        is_external=True,
                                    ),
                                ),
                                rx.cond(
                                    proyecto.demo_url != "",
                                    rx.link(
                                        rx.button("Ver demo", variant="solid"),
                                        href=proyecto.demo_url,
                                        is_external=True,
                                    ),
                                ),
                                spacing="3",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        padding="2em",
                        border_radius="10px",
                        border="1px solid rgba(255,255,255,0.08)",
                        background_color="rgba(255,255,255,0.02)",
                        _hover={"border_color": "rgba(255,255,255,0.15)", "background_color": "rgba(255,255,255,0.04)", "transform": "translateY(-2px)"},
                        transition="all 0.3s ease",
                        class_name="fade-in-up",
                    )
                ),
                class_name="proyectos-grid",
                width="100%",
            ),
            
            spacing="5",
            align_items="center",
            width="100%",
        ),
        id="proyectos",
        padding="4em 2em",
        background_color="#000000",
        on_mount=State.cargar_proyectos,
    )
