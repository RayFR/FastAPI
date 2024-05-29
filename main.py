from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4 # uuid library allows for usage and ensuring of unique identifiers

app = FastAPI() # create a new instance of FastAPI stored as the var app

class Task(BaseModel): # api will raise an exception if the data is not the correct data type pre determined 
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []

@app.post("/tasks/", response_model=Task) # uses this model to encode the json returned from this route
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=List[Task]) # get request endpoint at specified "/" URL 
def read_tasks():
    return tasks # fast API converts this data into JSON automatically

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task # if the requested task is valid with the task id return functions!
        
    return HTTPException(status_code=404, detail="Task Not Found!") # raises exception with status code 404 and a pre determined message

@app.put("/tasks/{task_id}", response_model=Task)

if __name__ == "__main__":
    import uvicorn # web server library

    uvicorn.run(app, host="0.0.0.0", port=8000) # runs the API app on the specified ports