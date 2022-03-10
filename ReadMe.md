# Курс Архитектура и шаблоны проектирования на Python
# GeekBrains

# Launching
```python
gunicorn -b address:port run:application
```
# URLS
Three urls available:
- /
- /contacts/
- /about/

Not found urls returns index page

# auth
For authorized request add to get request param "auth" with any value.
For example: http://127.0.0.1:8000/about?auth=11