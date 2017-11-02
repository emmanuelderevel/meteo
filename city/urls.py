from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'weather/(\d+)$', views.weather, name='weather'),
    url(r'find_city$', views.find_city, name='find_city'),
    url(r'login$', views.login, name='login'),
]
