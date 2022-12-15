from flask import Flask

app = Flask(__name__)


@app.route('/greet/<name>/')
def index(name: str):
    return f"Hello {name}!"

# @app.route("/greet/<name>/")
# def greet_name(name: str):
# return f"Hello {name}!"