import reflex as rx


def index() -> rx.Component:
    return rx.box(
        rx.text("¡Hola! Portfolio en construcción"),
        padding="2em",
        font_size="2em",
    )


app = rx.App()
app.add_page(index)