from typing import Any, Final

from random import SystemRandom as Random

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


PARAM_NAME: Final = "value"
ROUTE_PATH: Final = "/choice"


def choose_from_list(items: list[Any]) -> Any:
    return Random().choice(items)


def handle_request(request: Request) -> Response:
    passed_values: list[str] = request.query_params.getlist(PARAM_NAME)

    if not passed_values:
        return JSONResponse(content={"error": "No input values passed"})

    random_element: Any = choose_from_list(passed_values)
    return JSONResponse(content={PARAM_NAME: random_element})


app = Starlette()

app.add_route(ROUTE_PATH, handle_request, methods=["GET"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)