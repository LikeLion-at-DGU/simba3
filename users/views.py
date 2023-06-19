from django.shortcuts import render
from accounts.models import Profile
# Create your views here.

def detail_mypage(request):
    if request.method == 'POST':
        edit_profile = Profile.objects.get(user=request.user)
        edit_profile.age = request.POST['age']
        edit_profile.gender = request.POST['gender']
        edit_profile.major = request.POST['major']
        edit_profile.contact = request.POST['contact']
        edit_profile.about_me = request.POST['about_me']
        edit_profile.save()
        return render(request, 'users/mypage.html')
        pass
    else:
        return render(request, 'users/mypage.html')