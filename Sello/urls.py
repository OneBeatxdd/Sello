from django.contrib import admin
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /admin/
    url(r'^admin/', admin.site.urls),

    # /
    url(r'^$', views.index, name='index'),

    # /task/
    url(r'^task/', include(('task.urls', 'task'), namespace='task')),


    # /stickers/
    url(r'^stickers/1234', views.stickers, name='stickers'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
