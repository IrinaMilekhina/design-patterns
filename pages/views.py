from framework.views import BaseView

index_page = BaseView(
    context={
        "title": "Home page",
        "text": "Welcome to the simple WSGI application",
        "description": "Home text",
    },
    code="200 OK",
    template_name="index.html"
)

about_page = BaseView(
    context={
        "title": "About us",
        "text": "About us",
        "description": "Some text"
    },
    code="200 OK",
    template_name="about.html"
)

contacts_page = BaseView(
    context={
        "title": "Contacts",
        "text": "Our contacts",
        "email": "email@gmail.com",
        "phone": "+7 906 123-45-67"
    },
    code="200 OK",
    template_name="contacts.html"
)

