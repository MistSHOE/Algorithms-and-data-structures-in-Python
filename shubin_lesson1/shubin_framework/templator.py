# Используем стороний шаблонизатор Jinja2 v 3.0.3
from jinja2 import Template
from os.path import join


def render(name_template, folder='template', **kwargs):

    file_html = join(folder, name_template)

    with open(file_html, encoding='utf-8') as file:
        temp = Template(file.read())
    return temp.render(**kwargs)


# if __name__ == '__main__':
#     start_render = render('index.html',
#                           object_list=[{'name': 'Mistrun'},
#                                        {'name': 'Tao'}])
#     print(start_render)
