from app.models.student_model import Student
from app import db
from flask import request , jsonify

def create_student():
    try:
        data=request.get_json()
        if not data:
            return jsonify ({"error":"Data is required"}),400
        new_student=Student(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            date_of_birth=data["date_of_birth"]
        )
        db.session.add(new_student)
        db.session.commit()
        return jsonify ({"message":"Student added Successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error":"str(e)"})
    

def get_students():
    students=Student.query.all()
    students_list=[]
    for student in students:
        students_list.append({
            "student_id":student.student_id ,
            "first_name":student.first_name ,
            "last_name":student.last_name ,
            "email":student.email ,
            "date_of_birth":student.date_of_birth
        })
    return jsonify (students_list)


def get_student(student_id):
    student=Student.query.get(student_id)
    if not student:
        return jsonify ({"error":"Student not found"}),404
    return jsonify ({
        "student_id":student.student_id ,
        "first_name":student.first_name ,
        "last_name":student.last_name ,
        "email":student.email ,
        "date_of_birth":student.date_of_birth
    })


def update_student(student_id):
    try:
        data=request.get_json()
        student=Student.query.get(student_id)
        if not student:
            return jsonify ({"error":"Student not found"}),404
        student.first_name=data.get("first_name", student.first_name)
        student.last_name=data.get("last_name", student.last_name)
        student.email=data.get("email", student.email)
        student.date_of_birth=data.get("date_of_birth", student.date_of_birth)
        db.session.commit()
        return jsonify ({"message":"Student updated Successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error": (e)}), 400
    

def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not Found"})
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student Deleted Successfully!"})

