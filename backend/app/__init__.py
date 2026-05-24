from flask import Flask
from . import config

from . import extensions
from .models.user_model import UserModel
from .models.lesson_model import LessonModel
from .models.course_model import CourseModel

def create_app(config_class=config.Config, db=extensions.db, jwt_manager=extensions.jwt_manager):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    jwt_manager.init_app(app)

    # register blueprints

    @app.route("/api/test")
    def api_test():
        return {
            'message': "api works fine !"
        }
    
    return app
