from os.path import join

from jinja2 import Template

from framework.configs import TEMPLATES_DIR


def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    path = join(TEMPLATES_DIR, template_name)
    # Открываем шаблон по имени
    with open(path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)
