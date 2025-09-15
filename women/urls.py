from django.urls import path, register_converter, re_path

from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.archive, name='archive'),
]
