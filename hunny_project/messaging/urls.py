from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='messaging-home'),
    path('settings/', views.settings, name='messaging-settings'),
    
]