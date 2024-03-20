# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing all posts
    path('post/new/', views.post_new, name='post_new'),  # URL for creating a new post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # URL for editing a post
]
