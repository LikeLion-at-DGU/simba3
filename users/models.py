from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

# username 필드를 제거했기에 기존 유저 모델을 만드는 매서드에 username없이도 작동할 수 있도록 설정
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
# django에서 사용하는 AbstractUser를 상속받는 User 클래스 선언
class User(AbstractUser):
    # 기본 AbstractUser를 상속받아 수정
    username = None  # email만 사용할 것 이기에 제거
    email = models.EmailField(unique=True)  # email 필드를 주요 식별자로 사용

    USERNAME_FIELD = 'email'  # 인증 시 사용할 필드를 email로 설정
    REQUIRED_FIELDS = []  # createsuperuser 커맨드 사용 시 필요한 정보
    
    objects = UserManager()
    # 추가적인 필드들을 정의


