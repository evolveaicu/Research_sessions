# main.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Mock database
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

products_db = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 999},
    {"id": 2, "name": "Phone", "category": "electronics", "price": 599},
    {"id": 3, "name": "Desk", "category": "furniture", "price": 299}
]

# Get all items
@app.get("/users")
async def get_users(skip: int = 0, limit: int = 10):
    users_list = list(users_db.values())[skip:skip+limit]
    return {"users": users_list}

# Get specific item
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return user
    # return {"error": "User not found"}

# Get with filtering
@app.get("/products")
async def get_products(category: str = None, min_price: float = 0):
    filtered = products_db
    if category:
        filtered = [p for p in filtered if p["category"] == category]
    filtered = [p for p in filtered if p["price"] >= min_price]
    return {
        "category": category,
        "min_price": min_price,
        "products": filtered
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
