# main.py - Status Codes Demo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {"alice": {"email": "alice@test.com", "role": "user"}}

@app.get("/demo/200")
def success():
    """200 OK - Everything worked"""
    return {"message": "Success"}

@app.post("/demo/201")
def created():
    """201 Created - New resource created"""
    return {"message": "Resource created", "id": 123}

@app.get("/demo/400")
def bad_request():
    """400 Bad Request - Client sent invalid data"""
    raise HTTPException(
        status_code=400,
        detail="Invalid request format"
    )

@app.get("/demo/401")
def unauthorized():
    """401 Unauthorized - Authentication required"""
    raise HTTPException(
        status_code=401,
        detail="Please login first"
    )

@app.get("/demo/403")
def forbidden():
    """403 Forbidden - Authenticated but not allowed"""
    raise HTTPException(
        status_code=403,
        detail="You don't have permission to access this"
    )

@app.get("/demo/404")
def not_found():
    """404 Not Found - Resource doesn't exist"""
    raise HTTPException(
        status_code=404,
        detail="Resource not found"
    )

@app.post("/demo/409")
def conflict():
    """409 Conflict - Resource already exists"""
    raise HTTPException(
        status_code=409,
        detail="Username already taken"
    )

@app.get("/demo/422")
def validation_error():
    """422 Unprocessable Entity - Validation failed"""
    # This happens automatically with Pydantic
    raise HTTPException(
        status_code=422,
        detail="Validation failed"
    )

@app.get("/demo/500")
def server_error():
    """500 Internal Server Error - Something went wrong on server"""
    raise HTTPException(
        status_code=500,
        detail="Internal server error"
    )

if __name__ == "__main__":
    print("Visit each endpoint to see different status codes")
    uvicorn.run(app, host="0.0.0.0", port=8000)