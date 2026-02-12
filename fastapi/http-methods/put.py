# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from datetime import datetime

app = FastAPI()

# Mock database
users_db = {
    1: {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "age": 28,
        "bio": "Developer"
    }
}

class User(BaseModel):
    name: str
    email: str
    age: int
    bio: str

# Replace entire user
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "bio": user.bio,
        "updated_at": datetime.now().isoformat()
    }
    users_db[user_id] = updated_user
    return updated_user

# Get user to see changes
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)