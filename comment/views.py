from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Comment
from .forms import CommentForm
from video.models import Video

# Create your views here.

@login_required(login_url='/account/login/')
def add(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {'video': video}
    added = False

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.video = video
            post.save()
            added = True
            return HttpResponseRedirect(reverse('video:playback', kwargs={'video_id': video_id}))
        else:
            print(form.errors)
            err_context = {'video': video, 'error_msg': "Form is not properly filledin."}
            return render(request, 'comment/error.html', err_context)
    else:
        form = CommentForm()
        return render(request, 'video/playback.html', {'form': form})

