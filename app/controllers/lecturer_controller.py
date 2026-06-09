from app.models.lecturer_model import Lecturer
from app import db
from flask import request , jsonify

def create_lecturer():
    try:
        data=request.get_json()
        if not data:
            return jsonify ({"error":"Data is required"}),400
        new_lecturer=Lecturer(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            department=data["department"]
        )
        db.session.add(new_lecturer)
        db.session.commit()
        return jsonify ({"message":"Lecturer added Successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error":"str(e)"})
    

def get_lecturers():
    lecturers=Lecturer.query.all()
    lecturers_list=[]
    for lecturer in lecturers:
        lecturers_list.append({
            "lecturer_id":lecturer.lecturer_id ,
            "first_name":lecturer.first_name ,
            "last_name":lecturer.last_name ,
            "email":lecturer.email ,
            "department":lecturer.department
        })
    return jsonify (lecturers_list)


def get_lecturer(lecturer_id):
    lecturer=Lecturer.query.get(lecturer_id)
    if not lecturer:
        return jsonify ({"error":"Lecturer not found"}),404
    return jsonify ({
        "lecturer_id":lecturer.lecturer_id ,
        "first_name":lecturer.first_name ,
        "last_name":lecturer.last_name ,
        "email":lecturer.email ,
        "department":lecturer.department
    })


def update_lecturer(lecturer_id):
    try:
        data=request.get_json()
        lecturer=Lecturer.query.get(lecturer_id)
        if not lecturer:
            return jsonify ({"error":"Lecturer not found"}),404
        lecturer.first_name=data.get("first_name", lecturer.first_name)
        lecturer.last_name=data.get("last_name", lecturer.last_name)
        lecturer.email=data.get("email", lecturer.email)
        lecturer.department=data.get("department", lecturer.department)
        db.session.commit()
        return jsonify ({"message":"Lecturer updated Successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error": (e)}), 400
    

def delete_lecturer(lecturer_id):
    lecturer = Lecturer.query.get(lecturer_id)
    if not lecturer:
        return jsonify({"message": "Lecturer not Found"})
    db.session.delete(lecturer)
    db.session.commit()
    return jsonify({"message": "Lecturer Deleted Successfully!"})

