from wsgiref.simple_server import make_server
from shubin_lesson1.shubin_framework.main_framework import App
from urls import url_routes, fronts

# status = '200 OK'
# content = [('Content-Type', 'text/html')]
app = App(url_routes, fronts)

with make_server('127.0.0.1', 8211, app) as httpd:
    print("Обслуживание порта 8211")
    print('start')
    httpd.serve_forever()
