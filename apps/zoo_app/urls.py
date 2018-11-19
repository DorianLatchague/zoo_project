from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.zoo),
    url(r'^(?P<id>\d+)/build_store/(?P<location>\d+)$', views.build_store),
    url(r'^animal_store/(?P<id>\d+)/(?P<building_id>\d+)$', views.animal_store),
    url(r'^building/(?P<id>\d+)/(?P<building>\d+)$', views.building),
    url(r'^(?P<id>\d+)/manage$', views.manage),
    url(r'^(?P<id>\d+)/buy_building/(?P<location>\d+)$', views.buy_building),
    url(r'^buy_animal/(?P<id>\d+)/(?P<building>\d+)$', views.buy_animal),
    url(r'^ticket_price$', views.change_ticket_price),
    url(r'^buy_food/(?P<id>\d+)$', views.buy_food),
    url(r'^advance_day$', views.advance_day),
]