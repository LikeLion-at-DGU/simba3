from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User,Profile
import json,secrets
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        
        else:
            return render(request,'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                email=request.POST['email'],
                password=request.POST['password'],
            )

            auth.login(request,user)
            return redirect('/')
        nickname = request.POST['nickname']
        name = request.POST['name']

        profile = Profile(user = user,nickname=nickname,name=name)
        profile.save()

    return render(request,'accounts/signup.html')

def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        
        token = generate_auth_code(email)
        message = render_to_string('accounts/email_verify.html', {
            'token': token,
        })

        mail_title = "CO끼리 이메일 인증코드 발송"
        to_email = EmailMessage(mail_title, message, to=[email])
        to_email.send()

        response_data = {
            'message': 'Email 처리 완료',
            'email': email
        }
        return JsonResponse(response_data)

    # POST 요청 이외의 경우는 에러 처리
    response_data = {
        'error': 'Invalid request method'
    }
    return JsonResponse(response_data, status=400)



def generate_auth_code(email):
    # 임시 인증 코드 생성 로직
    auth_code = secrets.token_hex(4)
    # 캐시에 인증 코드 저장
    cache_key = f"auth_code_{email}"
    cache.set(cache_key, auth_code, timeout=600)  # 10분 동안 유효하도록 설정
    return auth_code

def verify_email(email, code):
    # 캐시에서 인증 코드 가져오기
    cache_key = f"auth_code_{email}"
    cached_code = cache.get(cache_key)

    if cached_code and cached_code == entered_code:
        cache.delete(cache_key)
        return True
    else:
        # 인증 코드가 일치하지 않는 경우
        return False