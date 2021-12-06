from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'
urlpatterns = [
    path('auth', views.detail, name='index'),
    path('', views.homepage, name='index'),
    path('<int:num>', views.productDetail, name='detail'),
    path('signup/', views.SignUpView.as_view(), name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
