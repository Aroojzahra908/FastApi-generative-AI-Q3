
from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "userName":"Ali",
    "rollNo": 2342
},
            {
    "userName":"Arooj zahra",   
    "rollNo": 9213
}
            ]
@app.get("/students")    # http://127.0.0.1:8080/students >> to access student data
def getStudents():
    return students

# dictionary of students data add one or more data to the dictionary
@app.get("/addStudent")
def addStudent(userName:str, rollNo:str):
    global students
    students.append({"userName":userName, "rollNo":rollNo})
    return students             # http://127.0.0.1:8080/addStudent and give query params 

@app.get("/")
def helloWorld():
    return {"hello": "world"}

@app.get("/gettodos/{userName}/{rollNo}")
def getTodos(userName:str, rollNo:str):
    print("Get todos called",userName,rollNo)
    return userName + rollNo 

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

# http://127.0.0.1:8080/getSingleTodo AND then give parameter name 
#like username called key and its name (aroojzahra) call value
@app.get("/getSingleTodo")
def getSingleTodo(userName:str, rollNo:str):
    print("Get todo called",userName,rollNo )
    return "get output without path variable called query parameters"


# for update we set put
@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"
    

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


