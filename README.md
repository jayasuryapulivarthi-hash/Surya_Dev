# Student Management REST API

A production-style backend application built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Docker**. This project demonstrates an end-to-end backend architecture by loading data from CSV files into PostgreSQL through an ETL pipeline and exposing RESTful APIs for managing academic data.

The application follows a clean layered architecture with separate Controller, Service, Repository, and Database layers to ensure scalability, maintainability, and separation of concerns.

---

## Project Overview

This project was developed to simulate a real-world backend system where data is extracted from CSV files, transformed using Pandas, loaded into PostgreSQL, and accessed through REST APIs.

The project emphasizes clean architecture, ORM-based database interactions, modular code organization, and containerized deployment using Docker.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3 |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Data Processing | Pandas |
| Validation | Pydantic |
| API Testing | Postman |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

---

## Project Architecture

```
                Client
                   │
                   ▼
          FastAPI Controllers
                   │
                   ▼
            Service Layer
          (Business Logic)
                   │
                   ▼
          Repository Layer
        (Database Operations)
                   │
                   ▼
          SQLAlchemy ORM
                   │
                   ▼
             PostgreSQL
```

---

## Folder Structure

```
Student-Management-API
│
├── app
│   ├── controllers
│   ├── services
│   ├── repositories
│   ├── schemas
│   ├── models
│   ├── etl
│   ├── database.py
│   └── main.py
│
├── data
│   ├── students.csv
│   ├── courses.csv
│   ├── instructors.csv
│   ├── enrollments.csv
│   └── courseinstructors.csv
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Features

- RESTful API development using FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- CSV to PostgreSQL ETL pipeline
- Data validation using Pydantic
- CRUD operations
- Modular layered architecture
- Dockerized application
- Interactive Swagger documentation
- API testing using Postman

---

## ETL Pipeline

The project includes a simple ETL pipeline built with Pandas.

### Workflow

```
CSV Files
    │
    ▼
Read using Pandas
    │
    ▼
Data Cleaning
    │
    ▼
Validation
    │
    ▼
Transformation
    │
    ▼
Load into PostgreSQL
```

The ETL process performs:

- Reading CSV files
- Data type conversion
- Data validation
- Null value handling
- Bulk insertion into PostgreSQL

---

## Database Models

The application currently manages the following entities:

- Students
- Courses
- Instructors
- Course Instructors

Each entity is represented using SQLAlchemy models and mapped to PostgreSQL tables.

---

## API Endpoints

The project currently supports CRUD operations for the available entities.

### Supported Operations

| Method | Description |
|---------|-------------|
| GET | Retrieve records |
| POST | Create new records |
| PUT | Update existing records |
| DELETE | Delete records |

---

## Running the Project

### Clone the Repository

```bash
git clone https://github.com/<your-username>/student-management-api.git

cd student-management-api
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

ReDoc Documentation

```
http://localhost:8000/redoc
```

---

## Running with Docker

### Build and Start Containers

```bash
docker compose up --build
```

Run in background

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

---

## Loading CSV Data

Run the ETL scripts to populate PostgreSQL.

Example

```bash
python -m app.etl.loadstudent_csv
```

---

## API Testing

The APIs can be tested using:

- Swagger UI
- Postman

---

## Skills Demonstrated

- Backend Development
- REST API Design
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- ETL Development
- Data Processing with Pandas
- Repository Pattern
- Service Layer Architecture
- MVC-inspired Project Structure
- Docker Containerization
- Git Version Control
- API Testing
- Database Modeling

---

## Future Enhancements

- JWT Authentication
- Role-Based Authorization
- Pagination
- Filtering & Search
- Logging
- Unit Testing
- Integration Testing
- CI/CD Pipeline
- Jenkins
- Kubernetes Deployment
- AWS Deployment
- Database Migrations with Alembic

---

## License

This project is intended for educational and portfolio purposes.

---

## Author

**Jayasurya Pulivarthi**

Backend Developer | Python | FastAPI | PostgreSQL | SQLAlchemy | Docker | Data Engineering

GitHub: https://github.com/<your-github-username>

LinkedIn: https://www.linkedin.com/in/<your-linkedin-profile>