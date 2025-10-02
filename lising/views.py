from django.http import *
from django.shortcuts import *
from django.urls import *
from django.template.defaultfilters import slugify


# Create your views here.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


equipment_db = [
    {'id': 1, 'name': 'Лизинг оборудования'},
    {'id': 2, 'name': 'Лизинг спецтехники'},
    {'id': 3, 'name': 'Лизинг транспорта'},
]

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Оборудование", 'url_name':
            'equipment'},
        {'title': "Обратная связь", 'url_name':
            'feedback'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Лизинг оборудования', 'content':
        'Станки, производственные линии, медицинское и IT-оборудование с минимальными первоначальными затратами',
     'is_published': True},
    {'id': 2, 'title': 'Лизинг спецтехники', 'content':
        'Экскаваторы, краны, бульдозеры и другая строительная техника на выгодных условиях.',
     'is_published': True},
    {'id': 3, 'title': 'Лизинг транспорта', 'content':
        'Грузовики, фуры, коммерческие автомобили с возможностью выкупа по окончании договора.',
     'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,  # не обязательная строчка
    }
    return render(request, 'leasing_equipment/index.html',
              context=data)


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'leasing_equipment/index.html',
                  context=data)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def equipment(request):
    return HttpResponse(f"Оборудование")


def login(request):
    return HttpResponse(f"Вход или регистрация")


def feedback(request):
    return HttpResponse(f"Обратная связь")


def about(request):
    return render(request, 'leasing_equipment/about.html', {'title': 'О сайте', 'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_category(request, cat_id):
    """Функция-заглушка"""
    return index(request)
