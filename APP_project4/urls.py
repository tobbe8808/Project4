from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news1/', views.news1),
    path('news2/', views.news2),
    path('admin/', admin.site.urls)
]