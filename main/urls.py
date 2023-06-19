from django.urls import path
from .views import *

app_name ="main"
urlpatterns = [
    path('', mainpage_competition, name="mainpage_competition"),
    path('mainpage_entrepreneur/', mainpage_entrepreneur, name="mainpage_entrepreneur"),
    path('mainpage_supporters/', mainpage_supporters, name="mainpage_supporters"),
]