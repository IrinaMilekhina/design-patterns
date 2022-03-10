from pages.render import render


def index_page(request):
    context = {
        "title": "Home page",
        "text": "Welcome to the simple WSGI application",
        "description": "Home text",
    }
    code = "200 OK"
    return code, render("index.html", context=context)


def about_page(request):
    context = {
        "title": "About us",
        "text": "About us",
        "description": "Some text"}
    code = "200 OK"
    return code, render("index.html", context=context)


def contacts_page(request):
    context = {
        "title": "Contacts",
        "text": "Our contacts",
        "email": "email@gmail.com",
        "phone": "+7 906 123-45-67",
    }
    code = "200 OK"
    return code, render("contacts.html", context=context)
