import json
import os

from framework import configs
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

        # TODO: check request.is_authorized

        view = self.urls.get_view(request)

        if request.action == 'POST':
            self.write_data_to_file(request, view.template_name)

        code = view.code
        text = view.render()
        start_response(code, headers)
        return [text.encode("utf-8")]

    @staticmethod
    def not_found_page() -> (str, str):
        return "404 Not found", "Page not found"

    @staticmethod
    def not_authorized() -> (str, str):
        return "403 Forbidden", "no token"

    @staticmethod
    def write_data_to_file(request: BaseRequest, template_name: str):
        data = request.post_body
        file_name = f"{template_name.split('.')[0]}.json"
        if not os.path.exists(configs.OUT_FILES_DIR):
            os.makedirs(configs.OUT_FILES_DIR)
        with open(os.path.join(configs.OUT_FILES_DIR, file_name), 'w+', encoding='utf-8') as f:
            json.dump(data, f)
