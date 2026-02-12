# main.py
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Mock database
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

posts_db = {
    1: {"id": 1, "user_id": 1, "title": "First Post", "content": "Hello World"},
    2: {"id": 2, "user_id": 1, "title": "Second Post", "content": "More content"}
}

# Delete user (returns message)
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    del users_db[user_id]
    return {"message": "User deleted successfully"}

# Delete user (returns 204 No Content)
@app.delete("/users-no-content/{user_id}", status_code=204)
async def delete_user_no_content(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    del users_db[user_id]
    return None

# Delete nested resource
@app.delete("/users/{user_id}/posts/{post_id}")
async def delete_post(user_id: int, post_id: int):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")

    del posts_db[post_id]
    return {"message": f"Post {post_id} deleted from user {user_id}"}

# View remaining users
@app.get("/users")
async def get_users():
    return {"users": list(users_db.values())}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)