from django.conf.urls import url
from . import views

urlpatterns = [
    # /task/
    url(r'^$', views.index, name='index'),


]