from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

def landing(request):
     return render(request, 'landing.html')

#lilly_note
@login_required(login_url='/landing')
def matchingroom(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     n_index = next_check_index(7, c_k)
     myprofile.current_check = n_index
     myprofile.save()
     first = Users.objects.filter()[(n_index):(n_index + 1)].get()
     context = {'first':first}
     return render(request,'matchingroom.html',context)

#lilly_note
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

#lilly_note
@login_required(login_url='/landing')
def like_next(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     c_k_profile = Users.objects.filter()[(c_k):(c_k + 1)].get()
     myprofile.who_like_me.add(c_k_profile)
     n_index = next_check_index(7, c_k)
     myprofile.current_check = n_index
     myprofile.save()
     next = Users.objects.filter()[(n_index):(n_index + 1)].get()
     context = {'next':next}
     return render(request, 'likenext.html',context)

#lilly_note
@login_required(login_url='/landing')
def dislike_next(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     n_index = next_check_index(7, c_k)
     myprofile.current_check = n_index
     myprofile.save()
     next = Users.objects.filter()[(n_index):(n_index + 1)].get()
     context = {'next':next}
     return render(request, 'dislikenext.html',context)

def next_check_index(max, current_index):
    if current_index == (max-1):
        return 0
    return (current_index + 1)


def terms_service(request):
     context = {}
     return render(request, 'terms_service.html',context)

@login_required(login_url='/landing')
def editProfile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if p_form.is_valid():
            p_form.save()
            return redirect('hunny-profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {'p_form': p_form}
    return render(request, 'profile-edit.html', context)

@login_required(login_url='/landing')
#lilly_note
def accountlogout(request):
    logout(request)
    return redirect('hunny-login')

#kody_note
@login_required(login_url='/landing')
def chat(request):
    return render(request, 'chat.html', {})

#kody_note
@login_required(login_url='/landing')
def chat_room(request, room_name):
    return render(request, 'chat_room.html', {'room_name': room_name})

#kody_note
@login_required(login_url='/landing')
def user(request):
    return render(request, 'user.html')



def home(request):
     return render(request, 'home.html')

@login_required(login_url='/landing')
def profile(request):
     return render(request, 'profile.html')

def message(request):
    return render(request, 'messages.html')

def user(request):
    return render(request, 'user.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#lilly_note
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
