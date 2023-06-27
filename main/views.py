from django.shortcuts import render
from post.models import Post, TrackKey, FieldKey
from django.db.models import Q


# Create your views here.
def mainpage_competition(request):
    competition = FieldKey.objects.get(fieldKey = "공모전")
    project = FieldKey.objects.get(fieldKey = "프로젝트")
    posts_com = competition.post.filter(isSave=True)
    posts_pro = project.post.filter(isSave=True)
    
    posts = posts_com.union(posts_pro)[:4]

    return render(request, 'main/mainpage_competition.html', {'posts':posts})

def mainpage_supporters(request):
    supporters = FieldKey.objects.get(fieldKey = "대외활동")
    posts = supporters.post.all()[:4]
    return render(request, 'main/mainpage_supporters.html', {'posts':posts})

def mainpage_entrepreneur(request):
    entrepreneur = FieldKey.objects.get(fieldKey = "창업")
    posts = entrepreneur.post.all()[:4]
    return render(request, 'main/mainpage_entrepreneur.html', {'posts':posts})

def search(request, f):
    if request.method == 'POST':
        typed_word = request.POST.get('word')  # 검색어
        selected_field = request.POST.get('field') # 모집 분야
        selected_track = request.POST.get('track') # 모집 트랙

        # word로 가져온 post 
        if typed_word == "":
            word_posts = Post.objects.filter(isSave = True)
            print(word_posts)
        else:
            word_posts = Post.objects.filter(title__contains = typed_word, isSave = True)

        # field로 가져온 post
        if selected_field != "전체":
            searched_field = FieldKey.objects.get(fieldKey = selected_field)
        # track으로 가져온 post
        if selected_track != "전체":
            searched_track = TrackKey.objects.get(trackKey = selected_track)

        if selected_field == "전체" and selected_track != "전체":
            posts = word_posts.filter(trackKey = searched_track)
        elif selected_track == "전체" and selected_field !="전체":
            posts = word_posts.filter(fieldKey = searched_field)
        elif selected_field !="전체" and selected_track != "전체":
            posts = word_posts.filter(Q(fieldKey = searched_field) & Q(trackKey = searched_track))
        elif selected_field == "전체" and selected_track == "전체":
            posts = word_posts

        return render(request, 'main/search.html', {'posts': posts})
    
    if request.method == 'GET':
        if f=='project':
            competition = FieldKey.objects.get(fieldKey = "공모전")
            project = FieldKey.objects.get(fieldKey = "프로젝트")
            posts_com = competition.post.all()
            posts_pro = project.post.all()
            posts = posts_com.union(posts_pro)
            return render(request, 'main/search.html', {'posts':posts})
        elif f=='supporters':
            supporters = FieldKey.objects.get(fieldKey = "대외활동")
            posts = supporters.post.all()
            return render(request, 'main/search.html', {'posts':posts})
        elif f=='entre':
            entrepreneur = FieldKey.objects.get(fieldKey = "창업")
            posts = entrepreneur.post.all()
            return render(request, 'main/search.html', {'posts':posts})




