# main.py - WITH ERROR HANDLING (Graceful Failures)
from fastapi import FastAPI, HTTPException
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
    if user_id not in users_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )
    return users_db[user_id]

@app.post("/transfer")
def transfer_money(transfer: Transfer):
    # Check if users exist
    if transfer.from_user not in users_db:
        raise HTTPException(
            status_code=404,
            detail=f"Sender user {transfer.from_user} not found"
        )

    if transfer.to_user not in users_db:
        raise HTTPException(
            status_code=404,
            detail=f"Recipient user {transfer.to_user} not found"
        )

    # Check sufficient balance
    if users_db[transfer.from_user]["balance"] < transfer.amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    # Check valid amount
    if transfer.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Transfer amount must be positive"
        )

    # Perform transfer
    users_db[transfer.from_user]["balance"] -= transfer.amount
    users_db[transfer.to_user]["balance"] += transfer.amount

    return {
        "message": "Transfer successful",
        "new_balance": users_db[transfer.from_user]["balance"]
    }

@app.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    result = a / b
    return {"result": result}

if __name__ == "__main__":
    print("This API handles errors gracefully!")
    print("Try: GET /users/999 (returns 404 with clear message)")
    print("Try: POST /divide with b=0 (returns 400 with clear message)")
    uvicorn.run(app, host="0.0.0.0", port=8000)