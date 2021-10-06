from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hunny-home'),
    path('profile/', views.profile, name='hunny-profile'),    
    path('messages/', views.messages, name='hunny-messages'),
    path('room/', views.messages_room, name='hunny-messages_room'),
]