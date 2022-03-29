# Курс Архитектура и шаблоны проектирования на Python
### GeekBrains

## Project structure
1. run.py
2. pages (directory)
   - templates (directory with html templates)
   - urls.py
   - views.py

## Quick start
create project structure

add view in to the view.py file:
```python
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
```
fill template for your index page (add index.html in the template folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ context.title }}</title>
</head>
<body>
<h1>
    {{ context.text }}
</h1>
<p>{{ context.description }}</p>
</body>
</html>
```

fill in the urls.py file:
```python
from framework.urls import BaseUrl
from pages.views import index_page

urlpatterns = [
    BaseUrl('/', index_page),
]
```

add run script:
```python
from framework.main import Framework
from pages.urls import urlpatterns

app = Framework(urlpatterns)
```
start it in the terminal!
```bash
gunicorn -b address:port run:application
```

and open http://127.0.0.1:8000/?auth=11 in browser 
## URLs
To add urls create templates/urls.py and use BaseUrl
```python
from framework.urls import BaseUrl
from pages.views import index_page

urlpatterns = [
    BaseUrl('/', index_page)
]
```
first argument is url and second is BaseView object

Not found urls returns 404 page

## Views
To add views create templates/views.py and use BaseView
```python
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
```
BaseView is the class with three requirement arguments:
- context: dict
- code: str
- template_name: str (must fully match the name of the file in the template folder) 


## auth
For authorized request add to get request param "auth" with any value.

For example: http://127.0.0.1:8000/about?auth=11