from fastapi import FastAPI , HTTPException
#creation de l'application
app =FastAPI()
#Creation de la root
@app.get("/")
def root():
    return {"message":"Bienvenue a FastApi"}
#Creation d'une liste des elements
items = []
@app.post("/items")
def create_item(item:str):
    items.append(item)
    return item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404,detail=f"Item {item_id} not found")


#JSON Request
@app.get("/items/")
def list_items(limit: int =10):
    return items[0:limit]

from pydantic import BaseModel
class Item(BaseModel):
    text: str = None
    is_done: bool = False