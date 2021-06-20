from flask import Flask
from flask_login import LoginManager

from .db import get_user


def create_app():
    """setup config"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dungnt196'
    app.config['APP_DB_URI'] = 'localhost:27017'
    app.config['APP_NS'] = 'tool_sicbo'

    """setup Login manager"""
    login_manager = LoginManager()
    login_manager.login_view = 'bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return get_user(email)


    from .bp import bp as bp
    app.register_blueprint(bp)

    return app