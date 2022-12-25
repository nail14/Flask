from time import time
from flask import Flask

from blog.article.view import article
from blog.user.views import user
from blog.report.views import report
# from flask import Flask, g
from flask import request

# создание приложения


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)

# app = Flask(__name__)
#
#
# @app.route('/')
# def index2():
#     return 'Hello web!'
#
#
# if __name__ == '__main__':
#     app.run()
#
#
# @app.route('/greet/<name>/')
# def index(name: str):
#     return f"Hello {name}!"

###################################################
# @app.route('/<string:search>', method=['GET','POST'])
# def index(search: str):
#     name = request.args.get('search', None)
#     return f"Hello {request.method}!"

# @app.route("/greet/<name>/")
# def greet_name(name: str):
# return f"Hello {name}!"
###################################################

# @app.errorhandler(404)
# def handler_404(error):
#     app.logger.error(error)
#     return 'ОШИБКА 404'
#
#
# @app.before_request
# def process_before_request():
#     """
#     Sets start_time to `g` object
#     """
#     g.start_time = time()
#
#
# @app.after_request
# def process_after_request(response):
#     """
#     adds process time in headers
#     """
#     if hasattr(g, "start_time"):
#         response.headers["process-time"] = time() - g.start_time
#
#     return response
