from django.conf.urls import url
from . import views

urlpatterns = [
    # /task/
    url(r'^$', views.index, name='index'),

    # /task/add
    url(r'^add/$', views.CreateTask.as_view(), name='task-add'),

    # /task/72/    <- task id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='task-detail')
]
