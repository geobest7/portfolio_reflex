import reflex as rx


def skeleton_proyecto() -> rx.Component:
    """Skeleton loader para proyecto mientras carga"""
    return rx.box(
        rx.vstack(
            # Título skeleton
            rx.box(
                height="28px",
                width="70%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="85%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            # Badges skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="70px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="55px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
                margin_top="1em",
            ),
            # Botones skeleton
            rx.hstack(
                rx.box(
                    height="36px",
                    width="100px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="36px",
                    width="100px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
                margin_top="1em",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="2em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
    )


def skeleton_curso() -> rx.Component:
    """Skeleton loader para curso mientras carga"""
    return rx.box(
        rx.vstack(
            # Tipo y título skeleton
            rx.hstack(
                rx.box(
                    height="20px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="60%",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
            ),
            # Institución skeleton
            rx.box(
                height="16px",
                width="50%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            # Fechas skeleton
            rx.box(
                height="14px",
                width="40%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            spacing="2",
            align_items="start",
        ),
        padding="1.5em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
        width="100%",
    )


def skeleton_experiencia() -> rx.Component:
    """Skeleton loader para experiencia mientras carga"""
    return rx.box(
        rx.vstack(
            # Cargo y empresa skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="24px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.vstack(
                    rx.box(
                        height="20px",
                        width="200px",
                        bg="#1a1a1a",
                        border_radius="4px",
                        class_name="skeleton-pulse",
                    ),
                    rx.box(
                        height="16px",
                        width="150px",
                        bg="#1a1a1a",
                        border_radius="4px",
                        class_name="skeleton-pulse",
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="start",
            ),
            # Fechas skeleton
            rx.hstack(
                rx.box(
                    height="20px",
                    width="20px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="16px",
                    width="180px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="90%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Tecnologías skeleton
            rx.hstack(
                rx.box(
                    height="24px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="70px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="24px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="12px",
                    class_name="skeleton-pulse",
                ),
                spacing="2",
            ),
            spacing="4",
            align="start",
        ),
        padding="1.5em",
        border_radius="8px",
        border="1px solid #333333",
        bg="#0a0a0a",
        width="100%",
    )


def skeleton_repo_github() -> rx.Component:
    """Skeleton loader para repo de GitHub mientras carga"""
    return rx.box(
        rx.vstack(
            # Nombre del repo skeleton
            rx.box(
                height="24px",
                width="60%",
                bg="#1a1a1a",
                border_radius="4px",
                class_name="skeleton-pulse",
            ),
            # Descripción skeleton (2 líneas)
            rx.box(
                height="16px",
                width="100%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.5em",
                class_name="skeleton-pulse",
            ),
            rx.box(
                height="16px",
                width="80%",
                bg="#1a1a1a",
                border_radius="4px",
                margin_top="0.3em",
                class_name="skeleton-pulse",
            ),
            # Stats skeleton (lenguaje, stars, forks)
            rx.hstack(
                rx.box(
                    height="20px",
                    width="80px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="20px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                rx.box(
                    height="20px",
                    width="60px",
                    bg="#1a1a1a",
                    border_radius="4px",
                    class_name="skeleton-pulse",
                ),
                spacing="3",
                margin_top="1em",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="1.5em",
        border_radius="8px",
        border="1px solid #333333",
        background_color="#0A0A0A",
        width="100%",
    )
