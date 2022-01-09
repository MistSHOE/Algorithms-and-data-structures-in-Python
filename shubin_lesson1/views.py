from shubin_lesson1.shubin_framework.templator import render
# Page controller


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', '<h1>Page About<h1>'


class Contacts:
    def __call__(self, request):
        return '200 OK', '<h1>Page Contacts<h1>'


class Error404:
    def __call__(self, request):
        return '200 OK', '<h1>Error 404 not page<h1>'


class Other:
    def __call__(self, request):
        return '200 OK', '<h1>Page Other<h1>'
