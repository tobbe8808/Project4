from django.contrib import admin
from django.urls import path, include
from . import views
from .views import post_view, like_post, home, Articledetails

urlpatterns = [
    path('', home.as_view(), name="index"),
    path('article/<int:pk>', Articledetails.as_view(), name='article-detail'),
    path('news2/', views.news2, name="news2"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', post_view, name='post-list'),
    path('like/', like_post, name='like-post'),

]