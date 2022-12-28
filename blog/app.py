from flask import Flask

from blog import commands
from blog.extensions import db, login_manager
from blog.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.user.views import user

    app.register_blueprint(user)
    app.register_blueprint(auth)


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)


# from time import time
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
#
# from blog import auth
# from blog.article.view import article
# from blog.user.views import user
# from blog.report.views import report
# # from flask import Flask, g
# from flask import request
#
#
# # создание приложения
#
#
# db = SQLAlchemy()
# # __all__ = [
# #     "db",
# # ]
#
#
# def create_app() -> Flask:
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'kwMhCoA7An6VtLzSkNOrVCpChSOIJ681'
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
#
#     db.init_app(app)
#
#     # from .models import User, Article
#
#     register_blueprints(app)
#     return app
#
#
# def register_blueprints(app: Flask):
#     app.register_blueprint(user)
#     app.register_blueprint(report)
#     app.register_blueprint(auth)
#     app.register_blueprint(article)
