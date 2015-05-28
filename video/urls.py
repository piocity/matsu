from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^upload/$', views.upload, name='upload'),
        url(r'^search/$', views.search, name='search'),
        url(r'^playback/(?P<video_id>[0-9]+)/$', views.playback, name='playback'),
]
