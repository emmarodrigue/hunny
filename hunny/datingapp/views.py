
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'datingapp/home.html', {})

def about(request):
    return HttpResponse('DATING APP ABOUT PAGE')

