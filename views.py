from simple_wsgi.views import BaseView
from simple_wsgi.decorators import route


@route('/')
class IndexView(BaseView):
    template_name = 'index.html'
    context = {
        'title': 'Template page',
        'text': 'Welcome to new WSGI framework!'
    }


class AboutView(BaseView):
    url = '/about/'
    text = 'About'
