from app.extensions import db

class CourseModel(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    lessons = db.relationship(
        'LessonModel',
        backref=db.backref('course', lazy=True),
        cascade='all, delete-orphan',
    )