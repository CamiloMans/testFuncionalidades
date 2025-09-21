from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []  # lista en memoria para guardar datos

# Endpoint GET en la raíz
@app.get("/")
def root():
    return {"Hello": "World"}

# Endpoint POST en /items
@app.post("/items")
def create_item(item: str):
    items.append(item)   # agrega el ítem a la lista
    return items          # devuelve lo que se agregó

@app.get("/items")
def get_items():
    return {"all_items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

git commit -m "Subiendo proyecto al repositorio testFuncionalidades"


