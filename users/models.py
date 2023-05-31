from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# django에서 사용하는 AbstractUser를 상속받는 User 클래스 선언
class User(AbstractUser):
    
    def __str__(self):
        return self.email
