from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='profile-home'),
    path('profile-edit/', views.editProfile, name='profile-edit'),
]