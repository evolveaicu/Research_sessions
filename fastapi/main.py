from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="My First API",
    description="This is my first FastAPI application",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint - Returns welcome message
    """
    return {"message": "Hello Backend"}

# Hello endpoint
@app.get("/hello")
async def hello():
    """
    Hello World endpoint
    """
    return {"message": "Hello World"}

# Greet with name
@app.get("/greet/{name}")
async def greet(name: str):
    """
    Greet a specific person

    - **name**: The name of the person to greet
    """
    return {"message": f"Hello {name}!"}

# Get info
@app.get("/info")
async def info():
    """
    API information endpoint
    """
    return {
        "app_name": "My First API",
        "version": "1.0.0",
        "description": "Learning FastAPI"
    }
