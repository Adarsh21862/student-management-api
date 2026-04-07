# Student Management System (REST API)

This is a beginner-to-intermediate level backend project built using Flask.  
It provides a RESTful API to manage student data with basic CRUD operations.

## Features
- Add new student
- Get all students
- Get student by ID
- Update student details
- Delete student

## Tech Stack
- Python
- Flask
- SQLite
- SQLAlchemy

## Project Structure
- app.py → Main application
- models.py → Database model
- routes.py → API routes
- config.py → Configuration

## API Endpoints

| Method | Endpoint | Description |
|-------|--------|------------|
| POST | /students | Add student |
| GET | /students | Get all students |
| GET | /students/<id> | Get student by ID |
| PUT | /students/<id> | Update student |
| DELETE | /students/<id> | Delete student |

## How to Run

```bash
pip install flask flask_sqlalchemy
python app.py
