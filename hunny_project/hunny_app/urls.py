from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='hunny-landing'),
    path('landing/', views.landing, name='hunny-landing'),
    path('signup/', views.signup, name='hunny-signup'),
    path('terms_service/', views.terms_service, name='hunny-terms_service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.accountlogin, name='hunny-login'),
    path('profile/', views.profile, name='hunny-profile'),    
    path('profile-edit/', views.editProfile, name='hunny-edit-profile'),
    path('message/', views.message, name='hunny-message'),
    path('matchingroom/', views.matchingroom, name='hunny-matchingroom'),
    path('like_next/', views.like_next, name='hunny-like'),
    path('dislike_next/', views.dislike_next, name='hunny-dislike'),
    path('user/', views.user, name='hunny-user'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),
    path('logout/', views.accountlogout, name='hunny-logout'),
    path('chat/', views.chat, name='hunny-chat'),
    path('chat/<str:room_name>/', views.chat_room, name='hunny-chat-room'),
<<<<<<< HEAD
    path('matchroom/', views.matchingroom, name='hunny-matchroom'),

    # user-specific routes
    path('user/', views.user, name='hunny-user'),
    path('settings/', views.settings, name='hunny-settings'),
    path('preferences/', views.preferences, name='hunny-preferences'),
    path('edit-preferences/', views.edit_preferences, name='hunny-edit-preferences'),
    path('profile/', views.profile, name='hunny-profile'),
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),
=======
>>>>>>> 6bddc099b05025ec85514ace8d6eb107b8e6c17a
]
