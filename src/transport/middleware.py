"""Special middleware for config envvar"""
from flask import request, abort


def middleware(req: request) -> request:
    injection: str = req.args.get("username", "")
    injection = "".join([letter for letter in injection if letter not in ["{", "}", " "]]).lower()
    match injection:
        case "config" | "session" | "g" | "config.popitem" | "config.pop":
            abort(400)
        case _:
            return req
