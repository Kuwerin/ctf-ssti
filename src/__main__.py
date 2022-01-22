import os
from typing import NoReturn

from transport.handler import flask_app


def main() -> NoReturn:
    """ Run the application"""
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = os.getenv("APP_PORT", "5000")
    flask_app.run(APP_HOST, APP_PORT)

main()
