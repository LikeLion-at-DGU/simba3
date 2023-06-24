from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('detail_profile/', detail_profile, name="detail_profile"),
    path('update_profile_pic/',update_profile_pic, name="update_profile_pic"),
    path('edit_portfolio/',edit_portfolio, name="edit_portfolio"),
    path('edit_profile/',edit_profile, name="edit_profile"),
]