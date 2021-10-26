from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth import authenticate, login

def landing(request):
     return render(request, 'landing.html')

def login(request):
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

def terms_service(request):
     return render(request, 'terms_service.html')

def home(request):
     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='/landing')
def profile(request):
     return render(request, 'profile.html')

@login_required(login_url='/landing')
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

@login_required(login_url='/landing')
def chat(request):
    return render(request, 'chat.html', {})

@login_required(login_url='/landing')
def chat_room_temp(request, room_name):
    return render(request, 'chat_room_temp.html', {'room_name': room_name})

@login_required(login_url='/landing')
def user(request):
    return render(request, 'user.html')

@login_required(login_url='/landing')
def settings(request):
    return render(request, 'settings.html')

@login_required(login_url='/landing')
def preferences(request):
    return render(request, 'preferences.html')

@login_required(login_url='/landing')
def matchingroom(request):
    context = {}
    return render(request, 'matchingroom.html', context)