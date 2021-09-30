from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Messages</h1>')

def settings(request):
    return HttpResponse('<h1>Settings</h1>')
