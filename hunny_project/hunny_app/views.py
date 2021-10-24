from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout

def landing(request):
     return render(request, 'landing.html')

def matchingroom(request):
    context = {}
    return render(request, 'matchingroom.html', context)

def accountlogin(request):
     if request.method == 'POST':
         user_name = request.POST.get('username')
         user_password = request.POST.get('password')
         user = authenticate(request, username=user_name, password=user_password)
         if user is not None:
             login(request, user)
             return redirect('hunny-profile')
         else:
             messages.info(request, "Username or Password is incorrect!")
     context = {}
     return render(request, 'login.html', context)

def terms_service(request):
     return render(request, 'terms_service.html')

def accountlogout(request):
    logout(request)
    return redirect('hunny-login')

def home(request):
     return render(request, 'home.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            redirect('hunny-initial')
        # else:
        #     messages.info(request, 'Username OR password is incorrect')
    
    context = {}
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def profile(request):
     return render(request, 'profile.html')

@login_required
def editProfile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('/profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'p_form': p_form}
    return render(request, 'profile_edit.html', context)


def message(request):
    return render(request, 'messages.html', {})

def messages_room(request, room_name):
    return render(request, 'messages_room.html', {'room_name': room_name})

def user(request):
    return render(request, 'user.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    form = CreateUserForm();
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,'Account was created successfully for ' + user_name )
            return redirect('hunny-login')
    context = {'form': form}
    return render(request, 'signup.html', context)

def settings(request):
    return render(request, 'settings.html')

def preferences(request):
    return render(request, 'preferences.html')

messages = [
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
