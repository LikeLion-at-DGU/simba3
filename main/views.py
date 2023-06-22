from django.shortcuts import render
from post.models import Post, TrackKey, FieldKey
from django.db.models import Q


# Create your views here.
def mainpage_competition(request):
    competition = FieldKey.objects.get(fieldKey = "competition")
    project = FieldKey.objects.get(fieldKey = "project")
    posts_com = competition.post.all()
    posts_pro = project.post.all()
    
    posts = posts_com.union(posts_pro)[:4]

    return render(request, 'main/mainpage_competition.html', {'posts':posts})

def mainpage_supporters(request):
    supporters = FieldKey.objects.get(fieldKey = "supporters")
    posts = supporters.post.all()[:4]
    return render(request, 'main/mainpage_supporters.html', {'posts':posts})

def mainpage_entrepreneur(request):
    entrepreneur = FieldKey.objects.get(fieldKey = "entrepreneur")
    posts = entrepreneur.post.all()[:4]
    return render(request, 'main/mainpage_entrepreneur.html', {'posts':posts})

def search(request):
    if request.method == 'POST':
        typed_word = request.POST.get('word')  # 검색어
        selected_field = request.POST.get('field') # 모집 분야
        selected_track = request.POST.get('track') # 모집 트랙
        print(typed_word, selected_field, selected_track)

        # word로 가져온 post 
        if typed_word == "":
            word_posts = Post.objects.all()
        else:
            word_posts = Post.objects.filter(title__contains = typed_word)

        # field로 가져온 post
        if selected_field != "all":
            searched_field = FieldKey.objects.get(fieldKey = selected_field)
        #     searched_field = FieldKey.objects.all()
        # else:
        #     searched_field = FieldKey.objects.get(fieldKey = selected_field)

        # track으로 가져온 post
        if selected_track != "all":
            searched_track = TrackKey.objects.get(trackKey = selected_track)
        #     searched_track = TrackKey.objects.all()
        # else:
        #     searched_track = TrackKey.objects.get(trackKey = selected_track)

        if selected_field == "all" and selected_track != "all":
            posts = word_posts.filter(trackKey = searched_track)
        elif selected_track == "all" and selected_field !="all":
            posts = word_posts.filter(fieldKey = searched_field)
        elif selected_field !="all" and selected_track != "all":
            posts = word_posts.filter(Q(fieldKey = searched_field) & Q(trackKey = searched_track))
        elif selected_field == "all" and selected_track == "all":
            posts = word_posts

        return render(request, 'main/search.html', {'posts': posts})


