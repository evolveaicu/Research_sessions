from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from datetime import datetime

app = FastAPI()

# Mock database
users_db = {}
posts_db = {}
next_user_id = 1
next_post_id = 1

# Define request body structure
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = None

class Post(BaseModel):
    title: str
    content: str

# Create new user
@app.post("/users")
async def create_user(user: User):
    global next_user_id
    new_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    users_db[next_user_id] = new_user
    next_user_id += 1
    return new_user

# Create nested resource
@app.post("/users/{user_id}/posts")
async def create_post(user_id: int, post: Post):
    global next_post_id
    new_post = {
        "id": next_post_id,
        "user_id": user_id,
        "title": post.title,
        "content": post.content,
        "created_at": datetime.now().isoformat()
    }
    posts_db[next_post_id] = new_post
    next_post_id += 1
    return new_post

# View created users
@app.get("/users")
async def get_users():
    return {"users": list(users_db.values())}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
