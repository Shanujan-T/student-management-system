from flask import Blueprint
from app.controllers import enrollment_controller

enrollment_bp=Blueprint("enrollment_bp",__name__)

@enrollment_bp.route('/api/enrollments', methods=["POST"])
def create_enrollment():
    return enrollment_controller.create_enrollment()

@enrollment_bp.route('/api/enrollments', methods=["GET"])
def get_enrollments():
    return enrollment_controller.get_enrollments()

@enrollment_bp.route('/api/enrollments/<int:enrollment_id>', methods=["GET"])
def get_enrollment(enrollment_id):
    return enrollment_controller.get_enrollment(enrollment_id)

@enrollment_bp.route('/api/enrollments/<int:enrollment_id>', methods=["PUT"])
def update_enrollment(enrollment_id):
    return enrollment_controller.update_enrollment(enrollment_id)

@enrollment_bp.route('/api/enrollments/<int:enrollment_id>', methods=["DELETE"])
def delete_enrollment(enrollment_id):
    return enrollment_controller.delete_enrollment(enrollment_id)