from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User,Profile
import json,secrets
from django.http import JsonResponse, HttpResponse
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
            return redirect('main:mainpage_competition')
        
        else:
            return render(request,'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def terms_of_use(request):
    return render(request,'accounts/terms_of_use.html')

def privacy(request):
    return render(request,'accounts/privacy.html')


def logout(request):
    auth.logout(request)
    return redirect("main:mainpage_competition")

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']

        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                email= email,
                password=request.POST['password'],
            )
            nickname = request.POST['nickname']
            name = request.POST['name']
            profile = Profile(user = user,nickname=nickname,name=name)
            profile.save()

            auth.login(request,user)
            return redirect('/')


    return render(request,'accounts/signup.html')

def delete_account(request):
    user = request.user
    user.delete()
    return render(request,'accounts/login.html')

def pw_finder(request):
    if request.method == 'POST':
        email = request.POST['email']
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.get(email = email)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('accounts:login')
    else:
        return render(request,'accounts/pw_finder.html')

def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if data.get('pagename') == 'pw_finder':
            if not User.objects.filter(email = email).exists():
                response_data = {
                'message': '존재하지 않는 이메일입니다.',
                }
                return JsonResponse(response_data)

        if User.objects.filter(email = email).exists():
            response_data = {
            'message': '이미 가입된 이메일입니다.',
            }
            return JsonResponse(response_data)
        dgu_domain_list = ['dongguk.edu','dgu.edu','dgu.ac.kr']
        domain = email.split('@')[1]
        if domain not in dgu_domain_list:
                response_data = {
                'message': '동국대학교 이메일을 사용해주세요.',
                }
                return JsonResponse(response_data)
        token = generate_auth_code(email)
        message = render_to_string('accounts/email_verify.html', {
            'token': token,
        })

        mail_title = "CO끼리 이메일 인증코드 발송"
        to_email = EmailMessage(mail_title, message, to=[email])
        to_email.send()

        response_data = {
            'email': email,
            'message': '인증번호 전송 완료',
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

def verify_email(request):
    # 캐시에서 인증 코드 가져오기
    data = json.loads(request.body)
    email = data.get('email')
    code = data.get('code')

    cache_key = f"auth_code_{email}"
    cached_code = cache.get(cache_key)

    if cached_code and cached_code == code:
        cache.delete(cache_key)
        return JsonResponse({'is_same': True})
    else:
        return JsonResponse({'is_same': False})
    

def nickname_redundant_check(request):
    data = json.loads(request.body)
    nickname = data.get('nickname')
    #만일 nickname이 중복될 때
    is_redundant = Profile.objects.filter(nickname=nickname).exists()
    if is_redundant:
        return JsonResponse({'is_redundant' : is_redundant})
    else:
        return JsonResponse({'is_redundnat' : is_redundant})
    