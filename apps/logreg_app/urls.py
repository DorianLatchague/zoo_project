from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logreg),
    url(r'^logging_in$', views.logging_in),
    url(r'^registering$', views.registering),
    url(r'^myaccount/(?P<id>\d+)$', views.edit),
    url(r'^myaccount/(?P<id>\d+)/edit', views.editing),
    url(r'^logout$', views.logout),
]
