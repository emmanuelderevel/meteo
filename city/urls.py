from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'weather/(\d+)$', views.weather, name='weather'),
    url(r'find_city$', views.find_city, name='find_city'),
    url(r'sign_up$', views.sign_up, name='sign_up'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'connexion$', views.connexion, name='connexion'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'alerts$', views.alerts, name='alerts'),
    url(r'^delete_alert/(\d+)$', views.delete_alert, name='delete_alert'),
    url(r'^create_alert/(\d+)/([\w\ \-]+)$', views.create_alert, name='create_alert'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),

]
