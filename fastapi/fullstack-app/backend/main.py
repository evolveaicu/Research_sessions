from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI()

# CORS - allows frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models - defines what data looks like
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    priority: int = Field(ge=1, le=5)

class Task(BaseModel):
    id: int
    title: str
    priority: int
    completed: bool
    created_at: str

# In-memory database
tasks = {
    1: {
        "id": 1,
        "title": "Learn FastAPI",
        "priority": 5,
        "completed": False,
        "created_at": datetime.now().isoformat()
    },
    2: {
        "id": 2,
        "title": "Build frontend",
        "priority": 4,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
}
next_id = 3

# Routes
@app.get("/api/tasks")
def get_tasks():
    return list(tasks.values())

@app.post("/api/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "priority": task.priority,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }

    tasks[next_id] = new_task
    next_id += 1

    return new_task

@app.patch("/api/tasks/{task_id}")
def update_task(task_id: int, completed: bool):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id]["completed"] = completed
    return tasks[task_id]

@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]