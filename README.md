# Simple WSGI

> Simple WSGI framework with Class-based views. Used jinja2 for templates.

Installation:
```
pip install -r requirements.txt
```
Run server:
```
gunicorn -b 127.0.0.1:8000 app:application -w3
```

## Usage

`app.py`

~~~ python
from simple_wsgi import Application
from views import IndexView, AboutView

views = [
    IndexView,
    AboutView
]

application = Application()
application.add_views(views)
~~~

`views.py`
~~~ python
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

~~~
