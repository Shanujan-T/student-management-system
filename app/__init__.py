from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.config import Config
from sqlalchemy import text
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.student_route import student_bp
    from app.routes.course_route import course_bp

    app.register_blueprint(student_bp)
    app.register_blueprint(course_bp)

    with app.app_context():
        db.session.execute(text("SELECT 1"))
        print("SUCCESS: Database Connected Successfully")
        db.create_all()

    return app 