from typing import Annotated

from fastapi import FastAPI, Path, Query

app: FastAPI = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(description="The ID of the item to get")],
    query: Annotated[str | None, Query(description="aboba")] = None
) -> dict[str, str | int | None]:
    return {"item_id": item_id, "query": query}
