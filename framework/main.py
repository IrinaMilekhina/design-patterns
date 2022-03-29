from framework.request import BaseRequest
from framework.urls import Urls


class Framework:

    def __init__(self, urls):
        self.urls = Urls(urls)

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        headers = [("Content-Text", "file/html")]
        request = BaseRequest(environ)

        if request.path_info not in self.urls.get_paths():
            code, text = self.not_found_page()
            start_response(code, headers)
            return [text.encode("utf-8")]

        view = self.urls.get_view(request)

        if request.is_authorized:
            code = view.code
            text = view.render()
        else:
            code = "403 Forbidden"
            text = "no token"
        start_response(code, headers)
        return [text.encode("utf-8")]

    @staticmethod
    def not_found_page() -> (str, str):
        return "404 Not found", "Page not found"
