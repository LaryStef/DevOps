from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    query: str | None = None
) -> dict[str, str | int | None]:
    return {"item_id": item_id, "query": query}
