from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.views import generic
from django.contrib.auth.decorators import login_required

from video.models import Video
from comment.models import Comment
from .forms import VideoForm
from comment.forms import CommentForm

# Create your views here.

@login_required(login_url='/account/login/')
def upload(request):
    context = RequestContext(request)
    uploaded = False

    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
#        if form.is_valid() and 'video_clip' in request.FILES:
        if form.is_valid():
#            if 'video_clip' in request.FILES:
 #               print("form valid but video_clip is not.")
            #return HttpResponse("form v, video_clip xdd")
            #video = form.save(commit=False)
            #video.video_clip = request.FILES['video_clip']
            #video.save()
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            uploaded = True

        else:
            print(form.errors)
            return render(request, 'video/upload.html', {'error_msg': "Form is not properly filled in."})

    else:
        form = VideoForm()

    return render_to_response('video/upload.html', {'form': form, 'uploaded': uploaded}, context)

def search(request):
    context = RequestContext(request)

    if request.method == "GET":
        results = Video.objects.filter(desc__icontains=request.GET.get('q', 'Find interesting video clips.'))
        return render(request, 'video/search.html', {'results': results})

def playback(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    # Might
    comments = list(Comment.objects.filter(video=video).order_by('-com_time'))
    comment_form = CommentForm()
    context = {'video': video, 'comments': comments, 'form': comment_form}
    return render(request, 'video/playback.html', context)

