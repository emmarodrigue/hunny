from django.shortcuts import render
from django.http import HttpResponse

messages = [
    {
    'recipient': 'Jessica Day',
    'message_contents': 'Hello!',
    'date_recieved': 'September 20, 2021',
    'date_delivered': 'September 21, 2021',
    'date_read': 'September 22, 2021',
    },
    {
    'recipient': 'Jane Hopkins',
    'message_contents': 'Hello how are you!',
    'date_recieved': 'September 22, 2021',
    'date_delivered': 'September 23, 2021',
    'date_read': 'September 24, 2021',
    },
    {
    'recipient': 'Jessica Day',
    'message_contents': 'Hello!',
    'date_recieved': 'September 20, 2021',
    'date_delivered': 'September 21, 2021',
    'date_read': 'September 22, 2021',
    },
    {
    'recipient': 'Jane Hopkins',
    'message_contents': 'Hello how are you!',
    'date_recieved': 'September 22, 2021',
    'date_delivered': 'September 23, 2021',
    'date_read': 'September 24, 2021',
    }
]

def home(request):
    context = {
        'messages': messages
    }
    return render(request, 'messaging/home.html', context)


def room(request):
    return render(request, 'messaging/room.html', {'recipient': 'Room'})
