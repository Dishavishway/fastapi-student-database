from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()

class OurBaseModel(BaseModel):
    class config:
        orm_mode = True

class student(OurBaseModel):
    id: int
    fname: str
    lname: str
    ismale: bool

@app.get('/',response_model=list[student], status_code=status.HTTP_200_OK)
def getALL_student():
    getAllStudents = db.query(models.student).all()
    return getAllStudents

@app.get('/getbyID/{studentID}', response_model=student, status_code=status.HTTP_200_OK)
def getbyID(studentID: int, Student:student):
    getStudent = db.query(models.student).filter(models.student.id == studentID).first()
    if getStudent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return getStudent

@app.post('/addstudent',response_model=student, status_code=status.HTTP_201_CREATED)
def add_student(Student:student):
    newStudent = models.student(
        id = Student.id,
        fname = Student.fname,
        lname = Student.lname,
        ismale = Student.ismale
    )
    find_student = db.query(models.student).filter(models.student.id == Student.id).first()

    if find_student is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= "Student with this ID already exist")
    
    db.add(newStudent)
    db.commit()

    return newStudent

@app.put('/update_student/{studentID}', response_model=student, status_code=status.HTTP_202_ACCEPTED)
def update_student(studentID: int, Student: student):
    find_student = db.query(models.student).filter(models.student.id == studentID).first()
    if not find_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    studentID = Student.id
    find_student.fname = Student.fname
    find_student.lname = Student.lname
    find_student.ismale = Student.ismale

    db.commit()
    return find_student

@app.delete('/deleteStudent/{studentID}', response_model=student, status_code=200)
def deleteStudent(studentID: int):
    find_student = db.query(models.student).filter(models.student.id == studentID).first()
    if not find_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="student with this id is either already deleted or not exist")
    db.delete(find_student)

    db.commit()
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Student is deleted successfully")
    