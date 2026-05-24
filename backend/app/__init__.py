from flask import Flask
from . import config

def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions

    # register blueprints

    @app.route("/api/test")
    def api_test():
        return {
            'message': "api works fine !"
        }
    
    return app
