from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('postpage/', postpage, name="postpage"),
    path('write/', write, name="write"),
    path('new/', new, name="new"),
    path('crew_search/<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]