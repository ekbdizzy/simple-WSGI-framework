import settings
from http.client import responses
from simple_wsgi.views import NotFoundView


class Application:

    def __init__(self, debug=settings.DEBUG):
        self.debug = debug
        self.views = {}

    def add_views(self, *args):
        self.views = {view.url: view for view in args[0]}
        return self.views

    def redirect_trailing_slash(self, path):
        view = self.views.get(path, NotFoundView)
        return view()

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            response = self.redirect_trailing_slash(path)

        else:
            view = self.views.get(path, NotFoundView)
            response = view()

        status_code = response.status_code
        start_response(
            f'{status_code} {responses[status_code]}',
            list(response.headers.items())
        )
        return [response.data().encode(encoding='utf-8')]
