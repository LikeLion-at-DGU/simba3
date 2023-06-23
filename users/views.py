from django.shortcuts import render,redirect
from accounts.models import Profile
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
        # update_profile.profile_pic = request.FILES.get('image')
        return redirect('users:detail_profile')

# update_post.image = request.FILES.get('image', update_post.image)