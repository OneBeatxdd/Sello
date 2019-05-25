from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # /admin/
    url(r'^admin/', admin.site.urls),

    # /
    url(r'^$', views.index, name='index'),
]
