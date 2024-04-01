
from fastapi import FastAPI
import uvicorn

# single route 
app = FastAPI()
@app.get("/items")
def getTodo():
    return "here to show we write: http://127.0.0.1:8080/items , here open route items " 

# route with variable
@app.get("/items/{items_id}")
def getTodo(items_id):
    return "here to show we write: http://127.0.0.1:8080/items/8 , here 8 is id we can write anything "

# route with variable and datatype int not accept string 
@app.get("/items2/{items2_id}")
def getTodo(items2_id:int):
    return {"here to show we write: http://127.0.0.1:8080/items/8 , here  is id we can write anything ": items2_id}

# route with variable and datatype string accept string and also int values but consider string in e.g "2"
@app.get("/items3/{items3_id}")
def getTodo(items3_id:str):
    return {"here to show we write: http://127.0.0.1:8080/items/Ali , here  is id we can write anything ": items3_id}

# declare a path parameter containing a path using a URL like:
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}    # http://127.0.0.1:8080/files/abc

# before item4 variable define name and after item variable define id  http://127.0.0.1:8080/toys/item4/666

@app.get("/{product_name}/item4/{product_id}")
def item4(product_name:str, product_id:int):
    return{"product_name":product_name, "product_id":product_id}  


def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)