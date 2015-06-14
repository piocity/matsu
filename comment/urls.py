from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
        url(r'^add/(?P<video_id>[0-9]+)/$', views.add, name='add'),
        url(r'^form/(?P<video_id>[0-9]+)/(?P<parent_id>[0-9]+)/$', views.add2, name='add2'),
]
