from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial, name='hunny-initial'),
    path('initial/', views.initial, name='hunny-initial'),
    path('terms_service/', views.terms_service, name='hunny-terms_service'),
    path('home/', views.home, name='hunny-home'),
    path('login/', views.login, name='hunny-login'),
    path('profile/', views.profile, name='hunny-profile'),    
    path('edit-profile/', views.editProfile, name='hunny-edit-profile'),
    path('messages/', views.messages, name='hunny-messages'),
    path('about/', views.about, name='hunny-about'),
    path('contact/', views.contact, name='hunny-contact'),
]