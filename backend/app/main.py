import os
from typing import List

try:
    import psycopg2
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False
    print("Warning: psycopg2 not installed. Database features will be disabled.")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "employeesdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


def get_connection():
    if not DB_AVAILABLE:
        raise Exception("Database not available. Please install psycopg2-binary.")
    return psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )


class Employee(BaseModel):
    id: int
    name: str
    role: str


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Employee Management API",
        "status": "running",
        "endpoints": {
            "employees": "/employees",
            "add_employee": "/employees (POST)",
            "docs": "/docs",
            "redoc": "/redoc",
        },
    }


@app.get("/employees", response_model=List[Employee])
def get_employees():
    if not DB_AVAILABLE:
        # Return mock data when database is not available
        return [
            {"id": 1, "name": "John Doe", "role": "Software Engineer"},
            {"id": 2, "name": "Jane Smith", "role": "Product Manager"},
            {"id": 3, "name": "Bob Johnson", "role": "DevOps Engineer"}
        ]
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, role FROM employees;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/employees", response_model=Employee)
def add_employee(emp: Employee):
    if not DB_AVAILABLE:
        # Return the employee back when database is not available
        return emp
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO employees (id, name, role) VALUES (%s, %s, %s);",
            (emp.id, emp.name, emp.role),
        )
        conn.commit()
        cur.close()
        conn.close()
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    if not DB_AVAILABLE:
        return {"status": "healthy", "database": "not_available", "note": "Running in mock mode"}
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
