from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/',signup,name="signup"),
    path('send_email/',send_email,name="send_email"),
    path('verify_email/',verify_email,name="verify_email"),
    path('pw_finder/',pw_finder,name="pw_finder"),
    path('delete_account/', delete_account,name="delete_account"),
    path('terms_of_use/',terms_of_use,name="terms_of_use"),
    path('privacy/',privacy,name="privacy"),
    path('nickname_redundant_check/',nickname_redundant_check,name="nickname_redundant_check"),
]