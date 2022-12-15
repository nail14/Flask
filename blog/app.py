from time import time

from flask import Flask, g
from flask import request

app = Flask(__name__)


@app.route("/")
def index2():
    return "Hello web!"


@app.route('/greet/<name>/')
def index(name: str):
    return f"Hello {name}!"


# @app.route('/<string:search>', method=['GET','POST'])
# def index(search: str):
#     name = request.args.get('search', None)
#     return f"Hello {request.method}!"

# @app.route("/greet/<name>/")
# def greet_name(name: str):
# return f"Hello {name}!"


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return 'ОШИБКА 404'


@app.before_request
def process_before_request():
    """
    Sets start_time to `g` object
    """
    g.start_time = time()


@app.after_request
def process_after_request(response):
    """
    adds process time in headers
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time

    return response
