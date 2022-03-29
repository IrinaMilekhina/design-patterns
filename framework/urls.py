from dataclasses import dataclass

from framework.request import BaseRequest
from framework.views import BaseView


@dataclass
class BaseUrl:
    url: str
    view: BaseView


class Urls:
    def __init__(self, urlpatterns):
        self.urlpatterns = urlpatterns

    def get_view(self, request: BaseRequest) -> BaseView:
        for url in self.urlpatterns:
            if url.url == request.path_info:
                return url.view

    def get_paths(self):
        return [url.url for url in self.urlpatterns]
