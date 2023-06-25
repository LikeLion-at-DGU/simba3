from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('write/', write, name="write"),
    path('new/', new, name="new"),
    path('crew_search/<int:id>', detail, name="detail"),
    path('temporary_save_post', temporary_save_post, name="temporary_save_post"),
    path('wrote_post', wrote_post, name="wrote_post"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]