from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Apply,FieldKey,TrackKey
from django.utils import timezone
import os

# 새로운 글 작성 페이지로 연결
def new(request):
    return render(request, 'post/post.html')

# Create
def write(request):
    new_post = Post()
    if request.FILES:
        new_post.image = request.FILES.get('image')
    else:
        new_post.image = 'default/post_image_default.jpg'
    new_post.team_name = request.POST['put_team']
    new_post.title = request.POST['put_subject']
    new_post.recruit_date = request.POST['put_date']
    new_post.link = request.POST['put_link']
    new_post.member = request.POST['put_member']
    new_post.about_us = request.POST['put_about_us']

    new_post.writer = request.user  # ForeignKey로 수정
    new_post.pub_date = timezone.now()

    if 'store_btn' in request.POST:
        new_post.isSave = False
        new_post.save()

        field_key = request.POST.get('fieldKey')
        f = FieldKey.objects.get(fieldKey=field_key)
        new_post.fieldKey.add(f.id)

        track_key = request.POST.get('trackKey')
        trackKey_list = track_key.split(',')
        for value in trackKey_list:
            t = TrackKey.objects.get(trackKey=value)
            new_post.trackKey.add(t.id)
        # 작성완료 누르면 crew_search 페이지로 이동
        return redirect('post:temporary_save_post')
    
    if 'submit_btn' in request.POST:
        new_post.isSave = True
        new_post.save()

        field_key = request.POST.get('fieldKey')
        f = FieldKey.objects.get(fieldKey=field_key)
        new_post.fieldKey.add(f.id)

        track_key = request.POST.get('trackKey')
        trackKey_list = track_key.split(',')
        for value in trackKey_list:
            t = TrackKey.objects.get(trackKey=value)
            new_post.trackKey.add(t.id)

        return redirect('post:wrote_post')

# 임시저장 글 목록페이지로 이동, 12-2. 글쓰기_임시저장
def temporary_save_post(request):
    posts = Post.objects.filter(writer=request.user, isSave=False)
    return render(request, 'post/temporary_save_post.html', {'posts':posts})

# 저장된글 목록페이지로 이동
def wrote_post(request):
    posts = Post.objects.filter(writer=request.user, isSave=True)
    return render(request, 'post/wrote_post.html', {'posts':posts})

# 글 상세페이지로 연결, 11-1 크루서치
def detail(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=id)
        return render(request, 'post/crew_search.html', {'post': post})
    if request.method == 'POST':
        new_apply = Apply()
        new_apply.short_text = request.POST['short_text']
        new_apply.writer = request.user
        new_apply.target_Post = get_object_or_404(Post, pk=id)
        new_apply.save()
        return  render(request, 'post/crew_search.html')
    
# post 페이지로 이동
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'post/post.html', {'post': edit_post})

# Update
# 수정 페이지
def update(request, id):
    update_post = Post.objects.get(id=id)
    # 수정할 때 이미지 수정 안하면 원래 이미지가 들어갈 수 있도록
    # 사진이 지워진 경우
    if request.FILES == None:
        # 기본 이미지가 이니라면 삭제 후 기본이미지 연결
        if update_post.image != 'default/post_image_default.jpg':
            os.remove(update_post.image.path)
            update_post.image = 'default/post_image_default.jpg'
    else:
        # 기본이미지가 아니면 지우고 저장
        if update_post.image != 'default/post_image_default.jpg':
            os.remove(update_post.image.path)
        update_post.image = request.FILES.get('image', update_post.image)
    update_post.team_name = request.POST['put_team']
    update_post.title = request.POST['put_subject']
    update_post.fieldKey = request.POST['fieldKey']
    update_post.trackKey = request.POST['trackKey']
    update_post.recruit_date = request.POST['put_date']
    update_post.link = request.POST['put_link']
    update_post.member = request.POST['put_member']
    update_post.about_us = request.POST['put_about_us']

    update_post.writer = request.user  # ForeignKey로 수정
    update_post.pub_date = timezone.now()

    update_post.save()
    return redirect('post:detail', update_post.id)

# Delete
def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('post:mainpage')
    # 삭제하면 어떤 페이지로 mainpage로 돌아간다(view의 mainpage 호출) -> 어떤 페이지로 돌아갈 것인지 추후 회의