from django.urls import path

from . import views

app_name = 'rating'
urlpatterns = [
    path('rate_product', views.rate_product, name='index'),
]
