from django.contrib import admin
from django.urls import path, include
from . import views
from .views import post_view, like_post

urlpatterns = [
    path('', views.index, name="index"),
    path('news1/', views.news1, name="news1"),
    path('news2/', views.news2, name="news2"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', post_view, name='post-list'),
    path('like/', like_post, name='like-post'),

]