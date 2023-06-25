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
    link = models.TextField(blank=True)
    member = models.TextField()
    about_us = models.TextField()

    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    isSave = models.BooleanField(default=False) # 저장할건지 안할건지 결정하는 field, 기본값 : 임시저장

    def __str__(self):  # title이 대표값
        return self.title

class Apply(models.Model):
    status_choices = (
        ('under_review', '검토중'),
        ('accept', '수락됨'),
        ('reject', '거절됨'),
    )
    writer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='apply', null=False,blank=False)
    target_Post = models.ForeignKey(Post, on_delete=models.CASCADE,null=False,blank=False)
    status = models.CharField(max_length=15,choices=status_choices,default='under_review')
    short_text = models.TextField(max_length=500)
    reply = models.TextField(max_length=100,null=True,blank=True)