import json
import functools


def to_json(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        json_data = json.dumps(func(*args, **kwargs))
        return json_data
    return new_func

