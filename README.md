# FastAPI Shipment Management API — MVC Refactor

A REST API for shipment management built with FastAPI, SQLModel, SQLite, and JWT-based authentication. This project reorganizes the shipment endpoints into a modular Model–View–Controller (MVC)-style architecture.

## Features

- User registration and login
- Password hashing using bcrypt
- JWT-based authentication
- Logout with token revocation
- Shipment CRUD operations
- Request validation using Pydantic and SQLModel
- Database sessions using SQLAlchemy and SQLModel
- Interactive API documentation with Swagger UI
- Modular routing, controller logic, model exports, and response formatting

## Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database ORM:** SQLModel / SQLAlchemy
- **Database:** SQLite by default; PostgreSQL configuration is supported
- **Authentication:** JWT, bcrypt
- **Validation:** Pydantic
- **API Testing:** Swagger UI
- **Version Control:** Git and GitHub

## Project Structure

```text
fastapi-shipment-api-mvc/
├── app/
│   ├── controllers/
│   │   └── shipment_controller.py
│   ├── models/
│   │   └── shipment.py
│   ├── routes/
│   │   └── shipment_routes.py
│   └── views/
│       └── shipment_view.py
├── database/
│   ├── models.py
│   └── sessions.py
├── api.py
├── auth.py
├── hash.py
├── schemas.py
├── requirements.txt
├── pyproject.toml
├── .env.example
└── README.md
```

### Architecture

- **Models:** Reuses the SQLModel shipment model defined in `database/models.py`, exposed to the application through `app/models/shipment.py`.
- **Views:** `app/views/shipment_view.py` formats individual shipment responses and shipment lists.
- **Controllers:** `app/controllers/shipment_controller.py` handles shipment operations and database interactions.
- **Routes:** `app/routes/shipment_routes.py` defines shipment API endpoints and delegates operations to the controller.
- **Application entry point:** `api.py` initializes the FastAPI application, database tables, and authentication endpoints.

## Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code or another Python editor

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vermayashi2006-maker/fastapi-shipment-api-mvc.git
cd fastapi-shipment-api-mvc
git switch mvc-refactor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run the following for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Review `.env` and configure the database URL and JWT settings. For local development, SQLite can be used.

**Security:** Replace the example JWT secret with a strong, private secret. Never commit your actual `.env` file or credentials to GitHub.

### 5. Start the application

```bash
python -m uvicorn api:app --reload
```

The application creates the database tables on startup.

## API Documentation

Once the server is running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/create-user` | Register a user |
| POST | `/login` | Authenticate and receive a JWT |
| GET | `/users/me` | Retrieve the authenticated user's profile |
| POST | `/logout` | Revoke the current JWT |
| POST | `/new-shipment` | Create a shipment |
| GET | `/shipments` | List shipments |
| GET | `/shipments/{shipment_id}` | Retrieve a shipment |
| PUT | `/shipments/{shipment_id}` | Replace a shipment |
| PATCH | `/shipments/{shipment_id}` | Partially update a shipment |
| DELETE | `/shipments/{shipment_id}` | Delete a shipment |

## Testing

Use Swagger UI at `/docs` to test the endpoints.

1. Register a user using `POST /create-user`.
2. Log in using `POST /login`.
3. Copy the returned JWT and authorize Swagger for protected user endpoints.
4. Test `GET /users/me` and `POST /logout`.
5. Test shipment creation, retrieval, updates, and deletion.

For logout verification, try the protected profile endpoint again with the revoked token; it should return `401 Unauthorized`.

## Learning Outcomes

- Building REST APIs with FastAPI
- Implementing CRUD operations
- Working with relational databases and ORM sessions
- Using JWT authentication and password hashing
- Organizing a backend application into MVC-style modules
- Separating request routing, business logic, and response formatting

## Project Background

This repository contains an MVC-style refactoring of a FastAPI shipment management training project. The refactoring focuses on modular organization and separation of responsibilities while retaining the existing authentication and shipment functionality.

## Future Improvements

- Add automated tests using Pytest and FastAPI's test client.
- Add shipment ownership and role-based access control.
- Introduce database migrations.
- Add pagination and filtering for shipment listings.
- Improve deployment configuration and security hardening.
