from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #기존에 제공하는 User 모델을 Profile 모델과 1ㄷ1 연결한다.
    name = models.TextField(max_length=10)
    nickname = models.TextField(max_length=10)
# Create your models here.
