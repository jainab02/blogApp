from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList,name='blogList'),
    path('create/', views.blogCreation,name='blogCreation'),
    path('<int:id>/update/', views.blogUpdate,name='blogUpdate'),
    path('<int:id>/delete>/', views.blogDelete,name='blogDelete'),
    path('register/', views.register,name='register'),
    path('logout/confirm/', views.logout_confirmation, name='logout_confirmation'),
    path('logout/', views.logout, name='logout'),
    path('<int:id>/blogRead/', views.blogRead, name='blogRead'),
    path('/blogSearch/', views.blogSearch, name='blogSearch'),
] 