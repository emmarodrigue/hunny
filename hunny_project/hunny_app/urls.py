from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hunny-home'),
    path('login/', views.login_request, name='login'),
    path('profile/', views.profile, name='hunny-profile'),    
    path('messages/', views.messages, name='hunny-messages'),
    path('message/room/', views.messages_room, name='hunny-messages_room'),
    path("register", views.register_request, name="register"),
]