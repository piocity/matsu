from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from video.models import Video

# Create your models here.

class Comment(models.Model):
    """Comment for a video."""
    contents = models.CharField('Comment', max_length=255)
    com_time = models.DateTimeField('Creation', default=timezone.now)
    author = models.ForeignKey(User)
    video = models.ForeignKey(Video)

    def __str__(self):
        return self.contents
