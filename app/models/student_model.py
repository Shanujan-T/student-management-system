from app import db

class Student(db.Model):
    __tablename__="students"
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)