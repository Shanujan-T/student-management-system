from flask import Blueprint
from app.controllers import course_controller

course_bp=Blueprint("course_bp",__name__)

@course_bp.route('/api/courses', methods=["POST"])
def create_course():
    return course_controller.create_course()

@course_bp.route('/api/courses', methods=["GET"])
def get_courses():
    return course_controller.get_courses()

@course_bp.route('/api/courses/<int:course_id>', methods=["GET"])
def get_course(course_id):
    return course_controller.get_course(course_id)

@course_bp.route('/api/courses/<int:course_id>', methods=["PUT"])
def update_course(course_id):
    return course_controller.update_course(course_id)

@course_bp.route('/api/courses/<int:course_id>', methods=["DELETE"])
def delete_course(course_id):
    return course_controller.delete_course(course_id)