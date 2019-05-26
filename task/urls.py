from django.conf.urls import url
from . import views

urlpatterns = [
    # /task/
    url(r'^$', views.index, name='index'),

    # /task/add
    url(r'^add/$', views.TaskCreate.as_view(), name='task-add'),

    # /task/72/    <- task id
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetails.as_view(), name='task-detail'),

    # /task/delete/70     <- task id
    url(r'^delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='task-delete'),

    # /task/update/
    url(r'^update/$', views.update_status, name='task-update')
]
