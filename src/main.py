from fastapi import FastAPI  # noqa: D100
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from reactpy.core.types import VdomDict

PICO_CSS = html.link(
    {
        "rel": "stylesheet",
        "href": "https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css",
    },
)


@component
def hello() -> VdomDict:
    """Sample api.

    Returns:
    -------
        VdomDict: _description_
    """
    count, set_count = use_state(0)

    def hundle_click(event):
        set_count(count + 1)

    return html.div({}, PICO_CSS, html.button({"on_click": hundle_click}, f"Hello, world! {count}"))


app = FastAPI()
configure(app, hello)
