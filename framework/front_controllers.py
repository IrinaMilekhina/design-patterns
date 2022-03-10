from urllib.parse import parse_qs


def request_method(environ):
    return environ.get("REQUEST_METHOD")


def auth_control(method, environ):
    if method == 'GET':
        queries = parse_qs(environ.get('QUERY_STRING'))
        queries = {k: v[0] for k, v in queries.items() if len(v) == 1}

        token = queries.get("auth")
    else:
        token = environ.get("auth")
    if token:
        return True
    else:
        return False


def front_controller(request, environ):
    request["action"] = request_method(environ)
    request["is_authorized"] = auth_control(request["action"], environ)


