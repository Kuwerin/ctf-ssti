"""Application main handlers"""

import os

from flask import (
    Flask,
    request,
    render_template_string,
)

from .middleware import middleware

flask_app = Flask("flask-app")

flask_app.config["APP_FLAG"] = os.getenv("APP_FLAG")

source_code = open(__file__).read()


@flask_app.route("/")
def index():
    template = """
    {% extends "index.html" %}
    {% block body %}
    <code>
    <pre>
    {{ source_code }}
    </pre>
    </code>
    {% endblock %}
    """
    return render_template_string(template, source_code=source_code)


@flask_app.route("/hello")
def hello_handler():
    middleware(request)
    name = request.args.get("username", "world")
    template = """
    {% extends "index.html" %}
    {% block body %}
    Hello, {}
    {% endblock %}
    """.replace("{}", name)
    return render_template_string(template)


@flask_app.route("/answer")
def help():
    template = """
    {% extends "index.html" %}
    {% block body %}
    <h1>The answer to the ultimate question of life, the universe and all that: {{ 7*6 }}</h1>
    <i>Douglas Adams
    {% endblock %}
    """
    return render_template_string(template)
