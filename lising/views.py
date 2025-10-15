from django.http import *
from django.shortcuts import *

from lising.models import Equipment, Category, TagPost


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
    posts = Equipment.objects.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'leasing_equipment/index.html',
                  context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Equipment.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,

        'cat_selected': None,
    }
    return render(request, 'leasing_equipment/equipment.html',
                  context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Equipment.objects.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'leasing_equipment/equipment.html',
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
    posts = Equipment.objects.all()
    data = {
        'title': 'Оборудование',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'leasing_equipment/equipment.html', context=data)


def login(request):
    return render(request, 'leasing_equipment/login.html', {'title': 'Вход или регистрация',
                                                            'menu': menu})


def feedback(request):
    return render(request, 'leasing_equipment/feedback.html', {'title': 'Обратная связь',
                                                               'menu': menu})


def about(request):
    return render(request, 'leasing_equipment/about.html', {'title': 'О сайте', 'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
