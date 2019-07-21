# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^restaurante/$', views.restaurante, name='restaurante'),
  url(r'^nuevo_restaurante/$', views.nuevo_restaurante, name='nuevo_restaurante'),
  url(r'^map_restaurante/$', views.map_restaurante, name='map_restaurante'),
  url(r'^grafica_restaurante/$', views.grafica_restaurante, name='grafica_restaurante'),
]