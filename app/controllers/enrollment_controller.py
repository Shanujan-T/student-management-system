from app.models.enrollment_model import Enrollment
from app import db
from flask import request , jsonify

def create_enrollment():
    try:
        data=request.get_json()
        if not data:
            return jsonify ({"error":"Data is required"}),400
        new_enrollment=Enrollment(
            student_id=data["student_id"],
            course_id=data["course_id"],
            enrollment_date=data["enrollment_date"],
            status=data.get("status", "Active")
        )
        db.session.add(new_enrollment)
        db.session.commit()
        return jsonify ({"message":"Enrollment added Successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error":str(e)})
    

def get_enrollments():
    enrollments=Enrollment.query.all()
    enrollments_list=[]
    for enrollment in enrollments:
        enrollments_list.append({
            "enrollment_id":enrollment.enrollment_id ,
            "student_id":enrollment.student_id ,
            "course_id":enrollment.course_id ,
            "enrollment_date":enrollment.enrollment_date ,
            "status":enrollment.status
        })
    return jsonify (enrollments_list)


def get_enrollment(enrollment_id):
    enrollment=Enrollment.query.get(enrollment_id)
    if not enrollment:
        return jsonify ({"error":"Enrollment not found"}),404
    return jsonify ({
        "enrollment_id":enrollment.enrollment_id ,
        "student_id":enrollment.student_id ,
        "course_id":enrollment.course_id ,
        "enrollment_date":enrollment.enrollment_date ,
        "status":enrollment.status
    })


def update_enrollment(enrollment_id):
    try:
        data=request.get_json()
        enrollment=Enrollment.query.get(enrollment_id)
        if not enrollment:
            return jsonify ({"error":"Enrollment not found"}),404
        enrollment.student_id=data.get("student_id", enrollment.student_id)
        enrollment.course_id=data.get("course_id", enrollment.course_id)
        enrollment.enrollment_date=data.get("enrollment_date", enrollment.enrollment_date)
        enrollment.status=data.get("status", enrollment.status)
        db.session.commit()
        return jsonify ({"message":"Enrollment updated Successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error": (e)}), 400
    

def delete_enrollment(enrollment_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if not enrollment:
        return jsonify({"message": "Enrollment not Found"})
    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment Deleted Successfully!"})

