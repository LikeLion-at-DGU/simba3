from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name ="main"
urlpatterns = [
    path('', start, name="start"),
    path('mainpage_competition', mainpage_competition, name="mainpage_competition"),
    path('mainpage_entrepreneur/', mainpage_entrepreneur, name="mainpage_entrepreneur"),
    path('mainpage_supporters/', mainpage_supporters, name="mainpage_supporters"),
    path('search/<str:f>', search, name="search"),
    path('guide/', guide, name="guide"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)