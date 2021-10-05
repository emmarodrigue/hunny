from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='messaging-home'),
    path('room/', views.room, name='messaging-room'),
    
]