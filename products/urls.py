from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'
urlpatterns = [
    path('auth', views.detail, name='index'),
    path('', views.homepage, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
