from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^add/(?P<video_id>[0-9]+)/$', views.add, name='add'),
]
