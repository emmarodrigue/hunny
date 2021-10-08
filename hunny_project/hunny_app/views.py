from django.shortcuts import render
from django.http import HttpResponse


def initial(request):
     return render(request, 'initial.html')

def terms_service(request):
     return render(request, 'terms_service.html')

def home(request):
     return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
     return render(request, 'profile.html')

def messages(request):
    return render(request, 'messages.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



message_list = [
    {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
    {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
    {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
    {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
        {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
        {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
        {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
        {
    'recipient': 'Recipient',
    'message_contents': 'Message',
    'date_recieved': 'Date Recieved',
    'date_delivered': 'Date Delivered',
    'date_read': 'Date Read',
    },
]