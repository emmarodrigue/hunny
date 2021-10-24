from django.urls import path, include
from . import views

app_name = 'chat'

urlpatterns = [
    # login/register routes
    path('', views.landing, name='hunny-landing'),
    path('landing/', views.landing, name='hunny-landing'),
    path('signup/', views.signup, name='hunny-signup'),
    path('terms_service/', views.terms_service, name='hunny-terms-service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.login, name='hunny-login'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),

    # messaging routes
    path('message/', views.message, name='hunny-messages'),
    path('messages/<str:room_name>/', views.messages_room, name='hunny-messages-room'),
    path('matchroom/', views.matchingroom, name='hunny-matchroom'),

    # user-specific routes
    path('user/', views.user, name='hunny-user'),
    path('settings/', views.settings, name='hunny-settings'),
    path('preferences/', views.preferences, name='hunny-preferences'),
    path('profile/', views.profile, name='hunny-profile'),
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),
]
