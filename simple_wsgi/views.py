import os
import settings
from jinja2 import Environment, FileSystemLoader


class BaseView:
    env = Environment(
        loader=FileSystemLoader(os.path.abspath(settings.TEMPLATE_DIRS))
    )
    url = ''
    text = 'Base view template'
    template_name = ''
    status_code = 200
    headers = {'Content-Type': 'text/html'}
    extra_headers = {}
    context = {}

    def data(self):
        """
        :return: template_name.render(context) or text
        """
        if self.template_name:
            return self.env.get_template(self.template_name).render(self.context)
        return self.text


class NotFoundView(BaseView):
    status_code = 404
    text = 'Ooops, this page not found'
