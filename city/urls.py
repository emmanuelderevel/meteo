from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'weather/(\d+)$', views.weather, name='weather'),
    url(r'find_city$', views.find_city, name='find_city'),
    url(r'sign_up$', views.signup, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'connexion$', views.connexion, name='connexion'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'alerts$', views.alerts, name='alerts'),
]
