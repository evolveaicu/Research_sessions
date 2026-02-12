# main.py - WITH VALIDATION (The Safe Way)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database
users_db = {}
next_id = 1

# Define what valid data looks like
class User(BaseModel):
    username: str
    email: str
    age: int
    bio: Optional[str] = None

@app.post("/api/users")
def create_user(user: User):
    """Only accept data matching the User model"""
    global next_id

    user_dict = user.dict()
    user_dict["id"] = next_id
    users_db[next_id] = user_dict
    next_id += 1

    return user_dict

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return users_db.get(user_id, {"error": "Not found"})

@app.get("/api/users")
def list_users():
    return list(users_db.values())

if __name__ == "__main__":
    print("This API validates all input!")
    print("Try sending invalid data - it will be rejected")
    uvicorn.run(app, host="0.0.0.0", port=8001)