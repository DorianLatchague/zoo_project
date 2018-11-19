from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$/(?P<id>\d+)', views.zoo),
    url(r'^build_store/(?P<id>\d+)/(?P<building>\d+)$', views.build_store),
    url(r'^animal_store/(?P<id>\d+)/(?P<building>\d+)$', views.animal_store),
    url(r'^building/(?P<id>\d+)/(?P<building>\d+)$', views.building),
    url(r'^manage/(?P<id>\d+)$', views.manage),
    url(r'^buy_building/(?P<id>\d+)/(?P<building>\d+)$', views.buy_building),
    url(r'^buy_animal/(?P<id>\d+)/(?P<building>\d+)$', views.buy_animal),
    url(r'^ticket_price$', views.change_ticket_price),
    url(r'^buy_food/(?P<id>\d+)$', views.buy_food),
    url(r'^advance_day$', views.advance_day),
]