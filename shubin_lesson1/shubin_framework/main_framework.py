from shubin_lesson1.views import Error404


class App:

    def __init__(self, url_routes, fronts):
        self.url_routes = url_routes
        self.fronts = fronts

    def __call__(self, environ, start_response):

        path_address = environ['PATH_INFO']
        # status = '200 OK'
        content = [('Content-Type', 'text/html')]

        if path_address in self.url_routes:
            views = self.url_routes[path_address]
        else:
            views = Error404()
        request = {}

        for front in self.fronts:
            front(request)

        code, body = views(request)

        start_response(code, content)
        return [body.encode('utf-8')]
