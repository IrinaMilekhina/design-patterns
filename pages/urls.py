from framework.urls import BaseUrl
from pages.views import index_page, about_page, contacts_page

urlpatterns = [
    BaseUrl('/', index_page),
    BaseUrl('/index/', index_page),
    BaseUrl('/contacts/', contacts_page),
    BaseUrl('/about/', about_page)
]
