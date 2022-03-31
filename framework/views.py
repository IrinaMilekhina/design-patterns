from os.path import join

from jinja2 import Template

from framework.configs import TEMPLATES_DIR


class BaseView:
    def __init__(self, context: dict, code: str, template_name: str):
        self.context = context
        self.code = code
        self.template_name = template_name

    def render(self):
        """
        Минимальный пример работы с шаблонизатором
        :param kwargs: параметры для передачи в шаблон
        :return:
        """
        path = join(TEMPLATES_DIR, self.template_name)
        with open(path, encoding='utf-8') as f:
            template = Template(f.read())
        return template.render(context=self.context)
