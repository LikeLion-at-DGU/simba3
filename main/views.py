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
        search_word = request.POST.get('word')  # 검색어
        selected_field = request.POST.get('field') # 모집 분야
        selected_track = request.POST.get('track') # 모집 트랙

        q = Q()
        # 모집분야에서 전체를 선택하면 검색 조건에 넣지 않는다
        if selected_field == 'all':
            q.add(Q(title__icontains=search_word), q.AND)   # 검색어를 포함하는 title
            q.add(Q(trackKey = selected_track), q.AND)      # 선택된 모집 트랙으로 검색
        # 모집트랙에서 전체를 선택하면 검색 조건에 넣지 않는다
        elif selected_track == 'all':
            q.add(Q(title__icontains=search_word), q.AND)   # 검색어를 포함하는 title
            q.add(Q(fieldKey = selected_field), q.AND)      # 선택된 모집 분야로 검색
        # 모집분야, 트랙 둘다 전체를 선택하면 검색어로만 검색
        elif selected_track == 'all' and selected_field == 'all':
            q.add(Q(title__icontains=search_word), q.AND)
        else:
            q.add(Q(title__icontains=search_word), q.AND)   # 검색어를 포함하는 title
            q.add(Q(fieldKey = selected_field), q.AND)      # 선택된 모집 분야로 검색
            q.add(Q(trackKey = selected_track), q.AND)      # 선택된 모집 트랙으로 검색
        post_list = Post.objects.filter(q) 

        return render(request, 'main/searchpage.html', {'post_list':post_list})


