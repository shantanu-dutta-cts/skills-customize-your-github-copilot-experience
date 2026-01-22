# 📘 Assignment: Building REST APIs using FastAPI

## 🎯 Objective

Learn to build a modern, high-performance REST API using FastAPI. You will create a fully functional API with multiple endpoints, data validation, and error handling to practice API design and backend development concepts.

## 📝 Tasks

### 🛠️ Create a Todo List API

#### Description
Build a RESTful API for managing a todo list with CRUD (Create, Read, Update, Delete) operations. This API should handle todo items with properties like title, description, completion status, and priority level.

#### Requirements
Completed API should:

- Implement a FastAPI application with proper project structure
- Create a data model using Pydantic for todo items with title, description, completed status, and priority fields
- Implement GET endpoint to retrieve all todo items
- Implement GET endpoint to retrieve a specific todo item by ID
- Implement POST endpoint to create a new todo item with validation
- Implement PUT endpoint to update an existing todo item
- Implement DELETE endpoint to remove a todo item
- Return appropriate HTTP status codes for success and error cases
- Include request/response documentation accessible via Swagger UI at `/docs`
- Handle edge cases such as invalid IDs and missing required fields with meaningful error messages

### 🛠️ Add Filtering and Sorting

#### Description
Extend the API to support filtering and sorting capabilities for better data retrieval and user experience.

#### Requirements
Completed API should:

- Add query parameters to filter todo items by completion status
- Add query parameters to sort todo items by priority or creation date
- Implement pagination support with limit and offset parameters
- Test endpoints with the Swagger UI interactive documentation
- Validate all query parameters and return clear error messages for invalid inputs
