# main.py - WITHOUT ERROR HANDLING (Crashes and Burns)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database
users_db = {
    1: {"name": "Alice", "balance": 100},
    2: {"name": "Bob", "balance": 50}
}

class Transfer(BaseModel):
    from_user: int
    to_user: int
    amount: float

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # This will crash if user doesn't exist!
    return users_db[user_id]

@app.post("/transfer")
def transfer_money(transfer: Transfer):
    # This will crash if users don't exist!
    users_db[transfer.from_user]["balance"] -= transfer.amount
    users_db[transfer.to_user]["balance"] += transfer.amount

    return {"message": "Transfer successful"}

@app.post("/divide")
def divide(a: float, b: float):
    # This will crash if b is zero!
    result = a / b
    return {"result": result}

if __name__ == "__main__":
    print("WARNING: This API crashes on errors!")
    print("Try: GET /users/999 (non-existent user)")
    print("Try: POST /divide with b=0")
    uvicorn.run(app, host="0.0.0.0", port=8000)