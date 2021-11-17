from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    path('signup/', views.signup, name='signup'),
    path('post/new', views.blog_new, name='blog_new'),
    path('post/<int:pk>/', views.blog_single, name='blog_single'),
    path('user/<int:author_id>/posts/', views.user_posts, name='user_posts'),
    path('post/<int:pk>/edit', views.blog_edit, name='blog_edit'),
    path('post/<int:pk>/delete', views.blog_delete, name='blog_delete'),
]