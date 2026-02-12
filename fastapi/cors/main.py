from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake in-memory DB
users_db = {
    1: {"id": 1, "username": "alice", "email": "alice@example.com", "age": 25},
}

next_id = 2

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(ge=18, le=120)

class User(UserCreate):
    id: int

@app.get("/api/users", response_model=List[User])
def get_users():
    return list(users_db.values())

@app.post("/api/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    global next_id

    for existing in users_db.values():
        if existing["username"] == user.username:
            raise HTTPException(
                status_code=409,
                detail="Username already exists"
            )

    new_user = {
        "id": next_id,
        **user.model_dump()
    }

    users_db[next_id] = new_user
    next_id += 1

    return new_user