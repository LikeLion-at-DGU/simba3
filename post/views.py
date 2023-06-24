from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

def postpage(request):
    return render(request, 'post/post.html')

# Create
def write(request):
    new_post = Post()
    new_post.image = request.FILES.get('image')
    new_post.team_name = request.POST['team_name']
    new_post.title = request.POST['title']
    new_post.fieldKey = request.POST['fieldKey']
    new_post.trackKey = request.POST['trackKey']
    new_post.recruit_date = request.POST['recruit_date']
    new_post.link = request.POST['link']
    new_post.member = request.POST['member']
    new_post.about_us = request.POST['about_us']

    new_post.writer = request.user  # ForeignKey로 수정
    new_post.pub_date = timezone.now()
    new_post.save()

    return redirect('post:detail', new_post.id)
    # 작성하면 게시글 detail을 보도록 이동 -> 어떤 화면이 보일지는 추후 회의

# 새로운 글 작성 페이지로 연결
def new(request):
    return render(request, 'post/new.html')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post/crew_search.html', {'post': post})

# Update 할 수 있는 페이지로 연결
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render('reqeust', 'post/edit.html', {'post': edit_post})

# Update
def update(request, id):
    update_post = Post.objects.get(id=id)
    # 수정할 때 이미지 수정 안하면 원래 이미지가 들어갈 수 있도록
    update_post.image = request.FILES.get('image', update_post.image)
    update_post.team_name = request.POST['team_name']
    update_post.title = request.POST['title']
    update_post.fieldKey = request.POST['fieldKey']
    update_post.trackKey = request.POST['trackKey']
    update_post.recruit_date = request.POST['recruit_date']
    update_post.link = request.POST['link']
    update_post.member = request.POST['member']
    update_post.about_us = request.POST['about_us']

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
