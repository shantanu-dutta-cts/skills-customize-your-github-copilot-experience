"""
FastAPI REST API - Todo List Application
This is starter code for building a todo list REST API using FastAPI.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(
    title="Todo List API",
    description="A REST API for managing todo items",
    version="1.0.0"
)

# Define the data model for a Todo item
class TodoItem(BaseModel):
    """Model for a todo item"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: int = 1  # 1 = low, 2 = medium, 3 = high


# Sample in-memory storage for todo items (replace with database in production)
todos_db: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastAPI", description="Study FastAPI fundamentals", completed=False, priority=3),
    TodoItem(id=2, title="Build API", description="Create a REST API", completed=False, priority=3),
]

# Counter for generating unique IDs
next_id = 3


# Root endpoint
@app.get("/")
def read_root():
    """Root endpoint - returns a welcome message"""
    return {"message": "Welcome to Todo List API"}


# TODO: Implement GET /todos endpoint to retrieve all todos
# Hint: Return the todos_db list


# TODO: Implement GET /todos/{todo_id} endpoint to retrieve a specific todo
# Hint: Search for the todo by ID in todos_db


# TODO: Implement POST /todos endpoint to create a new todo
# Hint: Generate a new ID, append to todos_db, return the created item


# TODO: Implement PUT /todos/{todo_id} endpoint to update a todo
# Hint: Find the todo, update its fields, return the updated item


# TODO: Implement DELETE /todos/{todo_id} endpoint to delete a todo
# Hint: Remove the todo from todos_db


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
