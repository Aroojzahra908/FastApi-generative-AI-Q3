# Query parameters:
# When you declare other function parameters that are not part of the path parameters, 
# they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

# run by using this url ---------- # http://127.0.0.1:8000/items/?skip=0&limit=1 

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# with additional paramter q and its data type
@app.get("/items1/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}          # for if part: http://127.0.0.1:8000/items1/100/?q=10
    
    return {"item_id": item_id}                      # for else part: http://127.0.0.1:8000/items1/100