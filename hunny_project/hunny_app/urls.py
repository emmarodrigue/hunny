from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.landing, name='hunny-landing'),
    path('landing/', views.landing, name='hunny-landing'),
    path('signup/', views.register, name='hunny-signup'),
    path('terms_service/', views.terms_service, name='hunny-terms-service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.login, name='hunny-login'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),

    path('profile/', views.profile, name='hunny-profile'),    
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),

    path('messages/', views.messages, name='hunny-messages'),
    path('messages/<str:room_name>/', views.messages_room, name='hunny-messages-room'),
    
    path('user/', views.user, name='hunny-user'),
    path('settings/', views.settings, name='hunny-settings'),

    path('matchroom/', views.matchroom, name='hunny-matchroom'),
    path('matchbox/', views.matchbox, name='hunny-matchbox'),

    path('preferences/', views.preferences, name='hunny-preferences'),
]