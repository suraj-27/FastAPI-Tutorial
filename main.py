"""
Fastapi tutorial with code with camp

Simple FastAPI student API example.

This module demonstrates:
- Basic FastAPI app setup with in-memory student data
- Pydantic models for request validation (Student, UpdateStudent)
- Endpoints for:
  - Listing/reading a single student by ID: /get_student/{student_id}
  - Searching students by name: /get_student_by_name/?name=...
  - Flexible search by ID or name: /get_student_by_any/?student_id=...&name=...
  - Creating a new student: /create_student/{student_id}
  - Partially updating a student: /update_student/{student_id}
  - Deleting a student: /delete_student/{student_id}

The home endpoint (/) returns a simple welcome message and is included in the API docs.
All endpoints use immediate in-memory storage (the `students` dict), so data is not persisted
across restarts. This is intended as a learning example, not a production system.
"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    year: int
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

app = FastAPI()

students = {
    1: {
        "name": "suraj",
        "age": 30,
        "year": 1993
    },
    2: {
        "name": "Ashwini",
        "age": 28,
        "year": 1996
    }
}

@app.get("/")
def index():
    return {"Message": "Welcome to Home Page"}

@app.get("/get_student/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student not found"}
    return students[student_id]

@app.get("/get_student_by_name/")
def get_student_by_name(name: Optional[str] = None):
    if name is None:
        return {"Error": "Name parameter is required"}
    for student_id in students:
        if students[student_id]["name"] == name:
            return {"Data": students[student_id]}
    return {"Error": "Data not found"}

@app.get("/get_student_by_any/")
def get_student_by_any(student_id: Optional[int] = None, name: Optional[str] = None):
    # If student_id is given
    if student_id is not None:
        if student_id in students:
            return students[student_id]
        return {"Data": "Not found"}
    
    # Fallback to name search
    if name is not None:
        for sid in students:
            if students[sid]["name"] == name:
                return students[sid]
        return {"Data": "Not found"}
    
    return {"Error": "Provide either student_id or name"}

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exist"}
    # Store as dict (or keep as Student if you want)
    students[student_id] = student.model_dump()
    return students[student_id]

@app.put("/update_student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student id not exist"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year
    
    return students[student_id]

@app.delete("/delete_student/{student_id}")
def delete_student(student_id: Optional[int]=None):
    if student_id not in students:
        return {"Error" : "Student not exist"}
    del students[student_id]
    return {"data" : students}
    