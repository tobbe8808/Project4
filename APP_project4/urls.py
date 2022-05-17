from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news1/', views.news1, name="news1"),
    path('news2/', views.news2, name="news2"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]