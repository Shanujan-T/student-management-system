from app.models.course_model import Course
from app import db
from flask import request , jsonify

def create_course():
    try:
        data=request.get_json()
        if not data:
            return jsonify ({"error":"Data is required"}),400
        new_course=Course(
            course_code=data["course_code"],
            course_name=data["course_name"],
            credits=data["credits"],
            lecturer_id=data["lecturer_id"]
        )
        db.session.add(new_course)
        db.session.commit()
        return jsonify ({"message":"Course added Successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error":"str(e)"})
    

def get_courses():
    courses=Course.query.all()
    courses_list=[]
    for course in courses:
        courses_list.append({
            "course_id":course.course_id ,
            "first_name":course.first_name ,
            "last_name":course.last_name ,
            "email":course.email ,
            "date_of_birth":course.date_of_birth
        })
    return jsonify (courses_list)


def get_course(course_id):
    course=Course.query.get(course_id)
    if not course:
        return jsonify ({"error":"Course not found"}),404
    return jsonify ({
        "course_id":course.course_id ,
        "course_code":course.course_code ,
        "course_name":course.course_name ,
        "credits":course.credits ,
        "lecturer_id":course.lecturer_id
    })


def update_course(course_id):
    try:
        data=request.get_json()
        course=Course.query.get(course_id)
        if not course:
            return jsonify ({"error":"Course not found"}),404
        course.course_code=data.get("course_code", course.course_code)
        course.course_name=data.get("course_name", course.course_name)
        course.credits=data.get("credits", course.credits)
        course.lecturer_id=data.get("lecturer_id", course.lecturer_id)
        db.session.commit()
        return jsonify ({"message":"Course updated Successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error": (e)}), 400
    

def delete_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"message": "Course not Found"})
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course Deleted Successfully!"})

