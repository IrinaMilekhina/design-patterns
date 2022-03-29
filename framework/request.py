from urllib.parse import parse_qs


class BaseRequest:
    def __init__(self, environ: dict):
        self.action = environ.get("REQUEST_METHOD")
        self.path_info = self._format_path(environ.get("PATH_INFO"))
        self.query_params = self._parse_queries(environ.get('QUERY_STRING'))
        self.auth = environ.get("auth")
        self.is_authorized = self._auth_control()
        self.headers = self._get_headers(environ)

    @staticmethod
    def _format_path(path_info):
        return path_info if path_info.endswith("/") else f"{path_info}/"

    @staticmethod
    def _parse_queries(query_string):
        return {k: v[0] for k, v in parse_qs(query_string).items() if len(v) == 1}

    def _auth_control(self):
        # TODO: change to token in headers
        if self.action == 'GET':

            token = self.query_params.get("auth")
        else:
            token = self.auth
        if token:
            return True
        else:
            return False

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith("HTTP"):
                key_name = key[5:].lower()
                headers[key_name] = value

        return headers
