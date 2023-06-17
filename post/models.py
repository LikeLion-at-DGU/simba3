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
    image = models.ImageField(upload_to='post/', blank=True, null=True)
    team_name = models.CharField(max_length=30, blank=False, default='')
    title = models.TextField(blank=False)
    fieldKey = models.ManyToManyField(FieldKey, related_name='field_Key', blank=False, default='')
    trackKey = models.ManyToManyField(TrackKey, related_name='track_Key', blank=False, default='')
    recruit_date = models.TextField(default='')
    link = models.TextField(default='')
    about_us = models.TextField(default='')

    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self):  # title이 대표값
        return self.title
