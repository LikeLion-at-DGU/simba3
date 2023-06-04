from django.shortcuts import render, redirect
from django.contrib import auth
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
