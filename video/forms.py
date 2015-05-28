from django import forms

from .models import Video

class VideoForm(forms.ModelForm):
    """A form for uploading new video clip."""
    class Meta:
        model = Video
        fields = ('title', 'desc', 'video_clip',)

