from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'datingapp-home'),
    path('about/', views.about, name = 'datingapp-about'),
    path('user/', views.user, name = 'datingapp-user'),
]
