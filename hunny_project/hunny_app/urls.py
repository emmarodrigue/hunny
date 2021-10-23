from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='hunny-home'),
    path('login/', views.login_request, name='login'),
=======
    path('', views.landing, name='hunny-landing'),
    path('landing/', views.landing, name='hunny-landing'),
    path('signup/', views.register, name='hunny-signup'),
    path('terms_service/', views.terms_service, name='hunny-terms_service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.login, name='hunny-login'),
>>>>>>> master
    path('profile/', views.profile, name='hunny-profile'),    
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),
    path('messages/', views.messages, name='hunny-messages'),
<<<<<<< HEAD
    path('message/room/', views.messages_room, name='hunny-messages_room'),
    path("register", views.register_request, name="register"),
=======
    path('user/', views.user, name='hunny-user'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),
>>>>>>> master
]