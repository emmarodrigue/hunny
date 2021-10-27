from django.urls import path, include
from . import views

app_name = 'chat'

urlpatterns = [
    # login/logout/register routes
    path('', views.landing, name='hunny-landing'),
    path('landing/', views.landing, name='hunny-landing'),
    path('signup/', views.signup, name='hunny-signup'),
    path('terms_service/', views.terms_service, name='hunny-terms-service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.login, name='hunny-login'),
    path('logout/', views.logout_user, name='hunny-logout'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),

    # messaging routes
    path('chat/', views.chat, name='hunny-chat'),
    path('chat/<str:room_name>/', views.chat_room, name='hunny-chat-room'),
    path('matchroom/', views.matchingroom, name='hunny-matchroom'),

    # user-specific routes
    path('user/', views.user, name='hunny-user'),
    path('settings/', views.settings, name='hunny-settings'),
    path('preferences/', views.preferences, name='hunny-preferences'),
    path('profile/', views.profile, name='hunny-profile'),
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),
]
