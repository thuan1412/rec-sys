from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('auth', views.detail, name='index'),
    path('', views.homepage, name='index'),
]