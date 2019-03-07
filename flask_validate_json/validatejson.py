from functools import wraps
from flask import request, g, abort
import re
from jsonschema import validate, ValidationError
from .custom_message import handle_failure
from .default_fill import DefaultValidatingDraft4Validator

def validate_json(schema={}, resp_func=lambda e: abort(400, e.message),force=False,custom_message=True,fill_defaults=False ):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            data = request.get_json(force=force)
            if data is None:
                return resp_func('can not decode json object')
            try:
                if fill_defaults:
                    DefaultValidatingDraft4Validator(schema).validate(data)
                else:
                    validate(data, schema)
            except ValidationError as e:
                if custom_message:
                    e.message = handle_failure(e,schema)
                return resp_func(e)
            g.json_data = data
            return func(*args, **kw)
        return wrapper
    return decorator