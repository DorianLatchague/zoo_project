from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.zoo_list),
    url(r'^create_zoo$', views.create_zoo),
    url(r'^creating_zoo$', views.creating_zoo),
    url(r'^(?P<id>\d+)$', views.zoo),
    url(r'^(?P<id>\d+)/build_store/(?P<location>\d+)$', views.build_store),
    url(r'^animal_store/(?P<building_id>\d+)$', views.animal_store),
    url(r'^building/(?P<building_id>\d+)$', views.building),
    url(r'^(?P<id>\d+)/manage$', views.manage),
    url(r'^(?P<id>\d+)/buy_building/(?P<location>\d+)$', views.buy_building),
    url(r'^(?P<building_id>\d+)/buy_animal$', views.buy_animal),
    url(r'^(?P<zoo_id>\d+)/ticket_price$', views.change_ticket_price),
    url(r'^buy_food/(?P<animal_id>\d+)$', views.buy_food),
    url(r'^advance_day$', views.advance_day),
    url(r'^leaderboard$', views.leaderboard),
    url(r'^user/(?P<user_id>\d+)', views.other_list),
]