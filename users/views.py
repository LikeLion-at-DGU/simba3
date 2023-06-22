from django.shortcuts import render,redirect
from accounts.models import Profile
# Create your views here.
def mypage(request):
    if request.method == 'POST':
        edit_profile = Profile.objects.get(user=request.user)
        edit_profile.age = request.POST['age']
        edit_profile.gender = request.POST['gender']
        edit_profile.major = request.POST['major']
        edit_profile.contact = request.POST['contact']
        edit_profile.about_me = request.POST['about_me']
        edit_profile.save()
        return render(request, 'users/mypage.html')

    else:
        if request.user is None:
            return redirect('accounts:login')
        else:
            profile = Profile.objects.get(user=request.user)
        return render(request, 'users/mypage.html', {'profile' : profile})