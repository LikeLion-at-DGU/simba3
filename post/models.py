from django.db import models
from users.models import User

class FieldKey(models.Model):
    fieldKey = models.CharField(max_length=30)

    def __str__(self):
        return self.fieldKey


class TrackKey(models.Model):
    trackKey = models.CharField(max_length=30)

    def __str__(self):
        return self.trackKey

class Post(models.Model):
    image = models.ImageField(upload_to='post/', blank=True, null=True, default='default/profile_pic_default.png')
    team_name = models.CharField(max_length=30, blank=False)
    title = models.TextField(blank=False)
    fieldKey = models.ManyToManyField(FieldKey, related_name='post', blank=False)
    trackKey = models.ManyToManyField(TrackKey, related_name='post', blank=False)
    recruit_date = models.TextField()
    link = models.TextField()
    about_us = models.TextField()

    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self):  # title이 대표값
        return self.title
