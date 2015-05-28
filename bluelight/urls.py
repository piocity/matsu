from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'bluelight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'bluelight.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^video/', include('video.urls', namespace='video')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
