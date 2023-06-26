from django.shortcuts import render,redirect
from django.utils import timezone
from accounts.models import Profile
from post.models import Apply,Post
import os
# Create your views here.
def mypage(request):
    if request.method == 'POST':
        edit_profile = Profile.objects.get(user=request.user)
        if request.POST['age'] :
            edit_profile.age = request.POST['age']
        else:
            edit_profile.age = None
        edit_profile.gender = request.POST['gender']
        edit_profile.major = request.POST['major']
        edit_profile.contact = request.POST['contact']
        edit_profile.about_me = request.POST['about_me']
        edit_profile.save()
        return render(request, 'users/mypage.html', {'profile':edit_profile })

    elif request.method == 'GET':
        profile = Profile.objects.get(user=request.user)
        return render(request, 'users/mypage.html', {'profile' : profile})

def detail_profile(request):
    if request.user is None:
        return redirect('accounts:login')
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'users/detail_profile.html', {'profile' : profile})

def edit_portfolio(request):
    if request.user is None:
        return redirect('accounts:login')
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request,'users/edit_portfolio.html',  {'profile' : profile})

def edit_profile(request):
    if request.user is None:
        return redirect('accounts:login')
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request,'users/edit_profile.html',  {'profile' : profile})

def update_profile_pic(request):
    update_profile = Profile.objects.get(user=request.user)
    if request.POST['action'] == "기본 이미지로 변경":
        if update_profile.profile_pic != 'default/profile_pic_default.png':
            os.remove(update_profile.profile_pic.path)
        update_profile.profile_pic = 'default/profile_pic_default.png'
        update_profile.save()
        return redirect('users:detail_profile')
    
    elif request.POST['action'] == '수정완료': 
        if len(request.FILES) != 0:
            if len(update_profile.profile_pic) > 0 and update_profile.profile_pic != 'default/profile_pic_default.png':
                os.remove(update_profile.profile_pic.path)
            update_profile.profile_pic = request.FILES['image']
            update_profile.save()
        return redirect('users:detail_profile')

def apply_manager(request, page):
    user = request.user
    profile = Profile.objects.get(user=user)
    if page == 'my_apply':
        applies = Apply.objects.filter(writer=user).order_by('-respond_date')
        return render(request,'users/apply_manager.html',{'profile': profile, 'applies' : applies, 'page' : page})
    elif page == 'rcv_apply':
        posts_by_user = Post.objects.filter(writer=user).order_by('-respond_date')
        applies = Apply.objects.filter(target_Post__in=posts_by_user)
        return render(request,'users/apply_manager.html',{'profile': profile, 'applies' : applies, 'page':page})

def detail_apply(request,page,id):
    apply = Apply.objects.get(id=id)
    profile = Profile.objects.get(user=apply.writer)
    if page == 'my_apply':
        return render(request, 'users/detail_my_apply.html',{'profile':profile, 'apply':apply})
    elif page == 'rcv_apply':
        return render(request, 'users/detail_rcv_apply.html',{'profile':profile, 'apply':apply})

def respond_apply(request,status,id):
    apply = Apply.objects.get(id=id)
    apply.reply = request.POST['reply']
    apply.status = status
    apply.save()
    pass