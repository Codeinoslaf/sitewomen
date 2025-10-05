from django.http import *
from django.shortcuts import *
from django.urls import *
from django.template.defaultfilters import slugify

from lising.models import Equipment


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


def index(request):
    posts = Equipment.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'leasing_equipment/index.html',
                  context=data)


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': Equipment.published.all(),
        'cat_selected': cat_id,
    }
    return render(request, 'leasing_equipment/index.html',
                  context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Equipment, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'post.html',
                  context=data)


def equipment(request):
    posts = Equipment.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'leasing_equipment/equipment.html', context=data)


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
