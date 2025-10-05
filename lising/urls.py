from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('equipment/', views.equipment, name='equipment'),
    path('login/', views.login, name='login'),
    path('feedback/', views.feedback, name='feedback'),
    path('post/<int:post_id>/', views.show_post,
         name='post'),
    path('category/<int:cat_id>/', views.show_category,
         name='category'),
    path('post/<slug:post_slug>/', views.show_post,
         name='post'),
]
