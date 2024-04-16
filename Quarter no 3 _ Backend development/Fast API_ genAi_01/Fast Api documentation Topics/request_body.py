# Request body:
#When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.                                  
# To declare a request body, you use Pydantic models with all their power and benefits                                        
# pip install pydantic

from fastapi import FastAPI
from  pydantic import BaseModel

class item(BaseModel):
    name:str
    Degree:str
    subject:str
    description:str
    fee:int 
    
app = FastAPI()


@app.post("/items")
def read_items(item:item):                                    # http://127.0.0.1:8000/items >>> and body mein json data jayega>> or json doc se aye ga .
# store data in database for store this schema 
    return item.name



# for update
@app.put("/items/{item_id}")
def update_item(item_id: int, item: item):
    return {"item_id": item_id, **item.dict()}                # http://127.0.0.1:8000/items/101



