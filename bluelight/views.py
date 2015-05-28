from django.shortcuts import render

from video.models import Video

def index(request):
    latest_videos = Video.objects.order_by('-upload_time')[:8]
    context = {'latest_videos': latest_videos}
    return render(request, 'bluelight/index.html', context)

