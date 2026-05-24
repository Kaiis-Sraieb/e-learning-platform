from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.course_model import CourseModel

course_bp = Blueprint('course_bp', __name__)


@course_bp.route("/courses", methods=["GET"])
def get_courses():

    courses = CourseModel.query.all()

    result = []

    for c in courses:
        result.append({
            "id": c.id,
            "title": c.title,
            "description": c.description
        })
        
    return jsonify(result)

@course_bp.route("/courses", methods=["POST"])
def create_course():

    data = request.get_json()

    new_course = CourseModel(
        title=data["title"],
        description=data["description"]
    )

    db.session.add(new_course)
    db.session.commit()

    return jsonify({
        "message": "course created",
        "new_course": new_course.to_dict()
    }), 201