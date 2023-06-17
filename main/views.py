from django.shortcuts import render

# Create your views here.

def mainpage_competition(request):
    return render(request, 'main/mainpage_competition.html')

def mainpage_supporters(request):
    return render(request, 'main/mainpage_supporters.html')

def mainpage_entrepreneur(request):
    return render(request, 'main/mainpage_entrepreneur.html')
