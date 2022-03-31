from urllib.parse import parse_qs


class BaseRequest:
    def __init__(self, environ: dict):
        self.action = environ.get("REQUEST_METHOD")
        self.path_info = self._format_path(environ.get("PATH_INFO"))
        self.query_params = self._parse_input_data(environ.get('QUERY_STRING'))
        self.headers = self._get_headers(environ)
        self.is_authorized = self._auth_control()
        self.post_body = self._get_request_boby(environ)

    @staticmethod
    def _format_path(path_info):
        return path_info if path_info.endswith("/") else f"{path_info}/"

    @staticmethod
    def _parse_input_data(query_string):
        return {k: v[0] for k, v in parse_qs(query_string).items() if len(v) == 1}

    def _get_request_boby(self, environ):
        if self.action == 'POST':
            content_length_data = environ.get('CONTENT_LENGTH')
            content_length = int(content_length_data) if content_length_data else 0
            data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
            data = self._parse_input_data(data.decode(encoding='utf-8'))
            return data

    def _auth_control(self):
        if self.headers.get('token') == '111':
            return True
        else:
            return False

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith("HTTP"):
                key_name = key[5:].lower()
                headers[key_name] = value
        headers['Accept-Encoding'] = 'UTF-8'
        headers['Content-Type'] = 'text/html'
        return headers
