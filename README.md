# FastAPI Student CRUD API

This project implements a RESTful API for managing student details using FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on student records.

## Features

- Create new student records
- Retrieve details of existing students
- Update student details
- Delete student records

## Technologies Used

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- PostgreSQL: An open-source relational database management system.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-student-crud.git
2. Install dependencies:

    cd fastapi-student-crud
    pip install -r requirements.txt

3.Set up the PostgreSQL database:
    Create a PostgreSQL database.
    Update the database URL in the SQLALCHEMY_DATABASE_URL variable in main.py to point to your PostgreSQL database.
4. Run the application:

    uvicorn main:app --reload

## Usage
Use the provided API endpoints to interact with the student database:
Create new students: POST /students/
Retrieve student details: GET /students/{student_id}
Update student details: PUT /students/{student_id}
Delete a student: DELETE /students/{student_id}
