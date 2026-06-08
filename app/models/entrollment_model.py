from app import db

class Entrollment(db.Model):
    __tablename__="entrollments"
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False, unique=True)
    status = db.Column(db.String(20), nullable=False)