from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model


def landing(request):
     return render(request, 'landing.html')

def signup(request):
     return render(request, 'signup.html')

def terms_service(request):
     return render(request, 'terms_service.html')

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

def profile(request):
     return render(request, 'profile.html')



def messages(request):
    return render(request, 'messages.html', {})

def messages_room(request, room_name):
    return render(request, 'messages_room.html', {'room_name': room_name})


def user(request):
    return render(request, 'user.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    form = CreateUserForm();
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, f'Account was created for {user}')
            
            return redirect('hunny-login')
        
    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required
def editProfile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been saved!')
            return redirect('/profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }

    return render(request, 'hunny_app/edit_profile.html', context)
