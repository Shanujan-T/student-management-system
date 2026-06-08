from flask import Blueprint
from app.controllers import student_controller

student_bp=Blueprint("student_bp",__name__)

@student_bp.route('/api/students', methods=["POST"])
def create_student():
    return student_controller.create_student()

@student_bp.route('/api/students', methods=["GET"])
def get_students():
    return student_controller.get_students()

@student_bp.route('/api/students/<int:student_id>', methods=["GET"])
def get_student(student_id):
    return student_controller.get_student(student_id)

@student_bp.route('/api/students/<int:student_id>', methods=["PUT"])
def update_student(student_id):
    return student_controller.update_student(student_id)

@student_bp.route('/api/students/<int:student_id>', methods=["DELETE"])
def delete_student(student_id):
    return student_controller.delete_student(student_id)