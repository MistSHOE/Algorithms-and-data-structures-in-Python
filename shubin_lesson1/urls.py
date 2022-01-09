from datetime import date
from views import Index, About, Contacts, Other

# front controller

url_routes = {
    '/': Index(),
    '/about': About(),
    '/contacts': Contacts(),
    '/other': Other()

}


def front_data(request):
    data = date.today()
    request['data'] = data


def front_text(request):
    my_text = ["Вы совершили переход на страницу"]
    request['text'] = my_text


fronts = [front_data, front_text]

