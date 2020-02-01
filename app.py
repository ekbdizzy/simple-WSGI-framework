from simple_wsgi import Application
from views import IndexView, AboutView

views = [
    IndexView,
    AboutView
]

application = Application()
application.add_views(views)

#  gunicorn -b 127.0.0.1:8000 app:application -w3
