# API Endpoints Documentation

This document provides details on the API endpoints for the project management module. All endpoints are available under the `/api/` prefix.

---

## Projects API

**Base URL**: `/api/projects/`

This API provides full CRUD (Create, Read, Update, Delete) functionality for projects.

### 1. List Projects

-   **Endpoint**: `GET /api/projects/`
-   **Description**: Retrieves a list of all projects.
-   **Success Response (200 OK)**:

    ```json
    [
        {
            "id": 1,
            "name": "Project Alpha",
            "code": "PA-01",
            "employer": 1,
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "progress": 50,
            "status": "in_progress"
        },
        {
            "id": 2,
            "name": "Project Beta",
            "code": "PB-02",
            "employer": 1,
            "start_date": "2024-02-01",
            "end_date": "2025-02-01",
            "progress": 10,
            "status": "planning"
        }
    ]
    ```

### 2. Retrieve a Project

-   **Endpoint**: `GET /api/projects/{id}/`
-   **Description**: Retrieves the details of a specific project by its ID.
-   **Success Response (200 OK)**:

    ```json
    {
        "id": 1,
        "name": "Project Alpha",
        "code": "PA-01",
        "description": "This is the first project.",
        "employer": 1,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "progress": 50,
        "status": "in_progress",
        "lat": 35.6892,
        "lng": 51.3890,
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-06-15T14:30:00Z"
    }
    ```

### 3. Create a Project

-   **Endpoint**: `POST /api/projects/`
-   **Description**: Creates a new project.
-   **Request Body**:

    ```json
    {
        "name": "New Project",
        "code": "NP-03",
        "employer": 2,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31"
    }
    ```

-   **Success Response (201 Created)**:

    ```json
    {
        "id": 3,
        "name": "New Project",
        "code": "NP-03",
        "employer": 2,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "progress": 0,
        "status": "planning"
    }
    ```

### 4. Update a Project (Full Update)

-   **Endpoint**: `PUT /api/projects/{id}/`
-   **Description**: Updates all fields of an existing project.
-   **Request Body**:

    ```json
    {
        "name": "Updated Project Name",
        "code": "PA-01-U",
        "employer": 1,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "progress": 75,
        "status": "in_progress"
    }
    ```

### 5. Partially Update a Project

-   **Endpoint**: `PATCH /api/projects/{id}/`
-   **Description**: Partially updates one or more fields of an existing project.
-   **Request Body**:

    ```json
    {
        "status": "completed",
        "progress": 100
    }
    ```

### 6. Delete a Project

-   **Endpoint**: `DELETE /api/projects/{id}/`
-   **Description**: Deletes a project.
-   **Success Response (204 No Content)**.

---

*Note: Similar CRUD endpoints will be implemented for `Phase` and `Activity` models as the project evolves.*
