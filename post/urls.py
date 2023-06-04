from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('write/', write, name="write"),
    path('new/', new, name="new"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]