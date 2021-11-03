from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.contrib.auth.models import User
import datetime

def landing(request):
     return render(request, 'landing.html')

@login_required(login_url='/landing')
def matchingroom(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     first = Users.objects.filter()[(c_k):(c_k + 1)].get()
     context = {'first':first}
     return render(request,'matchingroom.html',context)

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

@login_required(login_url='/landing')
def like_next(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     c_k_user = Users.objects.filter()[(c_k):(c_k + 1)].get()
     myprofile.who_like_me.add(c_k_user)
     n_index = next_check_index(Users.objects.count(), c_k)
     myprofile.current_check = n_index
     myprofile.save()
     add_match_if_bothlike(request.user,c_k_user)
     next = Users.objects.filter()[(n_index):(n_index + 1)].get()
     context = {'next':next}
     return render(request, 'likenext.html',context)

def add_match_if_bothlike(user1, user2):
    if user1 in user2.userprofile.who_like_me.all():
        user1.userprofile.matches.add(user2)
        user2.userprofile.matches.add(user1)
    return






@login_required(login_url='/landing')
def dislike_next(request):
     Users = get_user_model()
     myprofile= request.user.userprofile
     c_k = myprofile.current_check
     n_index = next_check_index(Users.objects.count(), c_k)
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
    return render(request, 'profile_edit.html', context)

def accountlogout(request):
    logout(request)
    return redirect('/landing')

@login_required(login_url='/landing')
def chat(request):
    user = User.objects.get(username=request.user)
    last_online = user.last_login.strftime('%a')
    return render(request, 'chat.html', {'last_online': last_online})

@login_required(login_url='/landing')
def chat_room(request, room_name):
    current_date = datetime.datetime.now()
    user = User.objects.get(username=request.user)
    last_online = user.last_login.strftime('%a')
    return render(request, 'chat_room.html', {'room_name': room_name,'current_date': current_date, 'last_online': last_online})

@login_required(login_url='/landing')
def user(request):
    return render(request, 'user.html')

def home(request):
     return render(request, 'home.html')

@login_required(login_url='/landing')
def profile(request):
     return render(request, 'profile.html')

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

@login_required(login_url='/landing')
def preferences(request):
    return render(request, 'preferences.html')

@login_required(login_url='/landing')
def editPreferences(request):
    p_form = ProfileUpdateForm()
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        if p_form.is_valid():
            p_form.save()
            return redirect('/preferences')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {'p_form':p_form}
    return render(request, 'preferences_edit.html', context)

@login_required(login_url='/landing')
def settings(request):
    return render(request, 'settings.html')
