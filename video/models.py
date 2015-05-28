from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    """
    The most important part of our BlueLight.
    """
    title = models.CharField('Title', max_length=255)
    desc = models.CharField('Description', max_length=1024)
    author = models.ForeignKey(User)
    upload_time = models.DateTimeField('Upload date', default=timezone.now)
    video_clip = models.FileField(upload_to='video')

    def __str__(self):
        return self.title

