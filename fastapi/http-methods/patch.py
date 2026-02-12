# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
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

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    bio: Optional[str] = None

# Update specific fields
@app.patch("/users/{user_id}")
async def partial_update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    existing_user = users_db[user_id].copy()

    # Update only provided fields
    update_data = user_update.dict(exclude_unset=True)
    existing_user.update(update_data)
    existing_user["updated_at"] = datetime.now().isoformat()

    users_db[user_id] = existing_user
    return existing_user

# Get user to see changes
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)