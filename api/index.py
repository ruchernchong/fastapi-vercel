from typing import Union

from fastapi import Depends, FastAPI, Response
from pydantic import BaseModel

app = FastAPI()


def add_cache_control(max_age: int = 3600):
    """Add Cache-Control header to response.

    Args:
        max_age: Cache duration in seconds (default: 1 hour)
    """
    def dependency(response: Response):
        response.headers["Cache-Control"] = f"public, max-age={max_age}"
    return dependency

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/", dependencies=[Depends(add_cache_control(31536000))])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", dependencies=[Depends(add_cache_control(31536000))])
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}