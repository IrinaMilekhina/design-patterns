from framework.front_controllers import front_controller
from pages.urls.urls import urlpatterns


class Framework:
    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        headers = [("Content-Text", "file/html")]
        path = environ.get("PATH_INFO")
        if not path.endswith("/"):
            path = f"{path}/"

        if path not in urlpatterns.keys():
            code, text = self.not_found_page()
            start_response(code, headers)
            return [text.encode("utf-8")]

        view = urlpatterns.get(path)
        request = {}
        front_controller(request, environ)
        if request.get("is_authorized"):
            code, text = view(request)
        else:
            code = "403 Forbidden"
            text = "no token"
        start_response(code, headers)
        return [text.encode("utf-8")]

    @staticmethod
    def not_found_page() -> (str, str):
        return "404 Not found", "Page not found"
