from django.shortcuts import render
from django.http import HttpResponse

def home(request):
     return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
     return render(request, 'profile.html')

def messages(request):
    context = {
        'message_list': message_list
    }
    return render(request, 'messages.html', context)

def messages_room(request):
    return render(request, 'messages_room.html', {'recipient': 'Room'})




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