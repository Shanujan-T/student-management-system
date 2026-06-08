from flask import Blueprint
from app.controllers import lecturer_controller

lecturer_bp=Blueprint("lecturer_bp",__name__)

@lecturer_bp.route('/api/lecturers', methods=["POST"])
def create_lecturer():
    return lecturer_controller.create_lecturer()

@lecturer_bp.route('/api/lecturers', methods=["GET"])
def get_lecturers():
    return lecturer_controller.get_lecturers()

@lecturer_bp.route('/api/lecturers/<int:lecturer_id>', methods=["GET"])
def get_lecturer(lecturer_id):
    return lecturer_controller.get_lecturer(lecturer_id)

@lecturer_bp.route('/api/lecturers/<int:lecturer_id>', methods=["PUT"])
def update_lecturer(lecturer_id):
    return lecturer_controller.update_lecturer(lecturer_id)

@lecturer_bp.route('/api/lecturers/<int:lecturer_id>', methods=["DELETE"])
def delete_lecturer(lecturer_id):
    return lecturer_controller.delete_lecturer(lecturer_id)