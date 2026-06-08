from app import db

class Course(db.Model):
    __tablename__="courses"
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    course_code = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False, unique=True)
    lecturer_id = db.Column(db.Integer, nullable=False)