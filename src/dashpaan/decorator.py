from functools import wraps
from json import loads as origin_loads
from dashpaan.json import dumps as patched_dumps


def rest(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)

        response = origin_loads(patched_dumps(response))

        return response

    return wrapper

