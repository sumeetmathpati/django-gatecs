from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile-own'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('register/', views.register, name='register')
]