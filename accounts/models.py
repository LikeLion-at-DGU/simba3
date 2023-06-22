from django.db import models
from users.models import User

def profile_pic_path(instance, filename):
	# MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    return f'profile_pics/user_{instance.pk}/{filename}'

class Profile(models.Model):
    gender_choices = (
        ('male', '남성'),
        ('female', '여성'),
        ('etc', '기타'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #기존에 제공하는 User 모델을 Profile 모델과 1ㄷ1 연결한다.
    name = models.TextField(max_length=10)
    nickname = models.TextField(max_length=10)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=8,choices=gender_choices,null=True)
    major = models.TextField(max_length=15,blank=True)
    contact = models.TextField(max_length=15,blank=True)
    about_me = models.TextField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to=profile_pic_path,default='default/profile_pic_default.png')
    def __str__(self):  # admin에서 표시될 user 필드 정보 설정
        return self.nickname

# Create your models here.