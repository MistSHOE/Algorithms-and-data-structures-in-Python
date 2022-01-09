
# начальные наброски кода

# if path_address == '/':
#     start_response(status, content)
#     return [b'Hello whis page index']
# elif path_address == '/about':
#     start_response(status, content)
#     return [b'Hello whis page about1']
# elif path_address == '/contacts':
#     start_response(status, content)
#     return [b'Hello whis page contacts']
# else:
#     start_response(status, content)
#     return [b'404 error page Mistrun']


#
# class Index:
#     def __call__(self, request):
#         return '200 OK', [b'<h1>Page Index<h1>']
#
#
# class About:
#     def __call__(self, request):
#         return '200 OK', [b'<h1>Page About<h1>']
#
#
# class Contacts:
#     def __call__(self, request):
#         return '200 OK', [b'<h1>Page Contacts<h1>']
#
#
# class Error404:
#     def __call__(self, request):
#         return '200 OK', [b'<h1>Error 404 not page<h1>']
#
#
# class Other:
#     def __call__(self, request):
#         return '200 OK', [b'<h1>Page Other<h1>']
#
#
# url_routes = {
#     '/': Index(),
#     '/about': About(),
#     '/contacts': Contacts(),
#     '/other': Other()
#
# }

# def front_data(request):
#     data = date.today()
#     request['data'] = data
#
#
# def front_text(request):
#     my_text = ["Вы совершили переход на страницу"]
#     request['text'] = my_text
#
#
# data_user = [front_data, front_text]