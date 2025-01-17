from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
