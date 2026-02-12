# main.py - WITHOUT VALIDATION (The Dangerous Way)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

@app.post("/api/users")
def create_user(user: dict):
    """Accept ANY data - no validation at all"""
    global next_id

    # Just blindly store whatever comes in
    user_id = next_id
    user["id"] = user_id
    users_db[user_id] = user
    next_id += 1

    return user

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return users_db.get(user_id, {"error": "Not found"})

@app.get("/api/users")
def list_users():
    return list(users_db.values())

if __name__ == "__main__":
    print("WARNING: This API accepts ANYTHING!")
    print("Try sending garbage data to /api/users")
    uvicorn.run(app, host="0.0.0.0", port=8000)