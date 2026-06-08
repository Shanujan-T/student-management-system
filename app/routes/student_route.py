from flask import Blueprint
from app.controllers import student_controller

student_bp=Blueprint("student_bp",__name__)

@student_bp.route('/api/students', methods=["POST"])
def create_student():
    return student_controller.create_student()

@student_bp.route('/api/students', methods=["GET"])
def get_students():
    return student_controller.get_students()

@student_bp.route('/api/students/<int:id>', methods=["GET"])
def get_student(id):
    return student_controller.get_student(id)

@student_bp.route('/api/students/<int:id>', methods=["PUT"])
def update_student(id):
    return student_controller.update_student_student(id)

@student_bp.route('/api/students/<int:id>', methods=["DELETE"])
def delete_student(id):
    return student_controller.delete_student(id)