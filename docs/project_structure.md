# Project Structure Documentation

This document describes the directory and file structure of the backend application, following best practices for a Django project.

## Root Directory (`backend/`)

The main directory for the Django project.

```
backend/
├── apps/
│   └── projects/
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs/
│   ├── api_endpoints.md
│   ├── database_schema.md
│   └── project_structure.md
├── manage.py
└── README.md
```

### `apps/`

This directory contains the different applications (modules) of the project. Each app is self-contained.

-   **`apps/projects/`**: This is the application for managing projects, phases, and activities.
    -   `models.py`: Contains the Django models (`Project`, `Phase`, `Activity`, `Dependency`).
    -   `serializers.py`: Contains the DRF serializers for the models.
    -   `views.py`: Contains the API views (ViewSets) for handling CRUD operations.
    -   `urls.py`: Defines the URL routes for the `projects` app.
    -   `admin.py`: Registers the models with the Django admin site.
    -   `apps.py`: App configuration.
    -   `tests.py`: For writing unit and integration tests.

### `backend/` (Project Configuration)

This directory contains the main project configuration files.

-   `settings.py`: Django settings for the project (database, installed apps, etc.).
-   `urls.py`: The root URL configuration for the entire project. It includes the URLs from the different apps.

### `docs/`

This directory holds all the project documentation.

-   `database_schema.md`: Documentation for the database models.
-   `api_endpoints.md`: Documentation for the API endpoints.
-   `project_structure.md`: This file.

### Root Files

-   `manage.py`: The command-line utility for interacting with the Django project.
-   `README.md`: The main README file for the project, providing an overview and setup instructions.
