from functools import wraps

from dashpaan.django import JsonResponse

from dashpaan.json import loads as origin_loads
from dashpaan.json import JSONEncoder, dumps as patched_dumps


def rest(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)

        response = origin_loads(patched_dumps(response))

        return response

    return wrapper


def page(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        return JsonResponse(view_func(request, *args, **kwargs), encoder=JSONEncoder, status=200)

    return wrapper
