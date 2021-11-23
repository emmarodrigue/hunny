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
     next = Users.objects.filter()[(c_k):(c_k + 1)].get()
     context = {'next':next}
     return render(request,'dislikenext.html',context)

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
    return searching_process(request, 1)

@login_required(login_url='/landing')
def dislike_next(request):
    return searching_process(request, 0)

def searching_process(request, like):
     Users = get_user_model()
     myprofile= request.user.userprofile
     current_check = myprofile.current_check
     next_check = next_check_index(Users.objects.count(), current_check)
     myprofile.current_check = next_check
     myprofile.save()
     next = Users.objects.filter()[(next_check):(next_check + 1)].get()
     if like == 1:
        current_check_user = Users.objects.filter()[(current_check):(current_check + 1)].get()
        myprofile.who_like_me.add(current_check_user)
        match = add_match_if_bothlike(request.user, current_check_user)
        context = {'next':next, 'match':match}
        return render(request, 'likenext.html', context)
     if like == 0:
        context = {'next':next}
        return render(request, 'dislikenext.html',context)

def add_match_if_bothlike(user1, user2):
    if user1 in user2.userprofile.who_like_me.all():
        user1.userprofile.matches.add(user2)
        user2.userprofile.matches.add(user1)
        user2.userprofile.who_like_me.remove(user1)
        user1.userprofile.who_like_me.remove(user2)
        return 1
    return 0

def filter(user):
    gender = user.userprofile.gender_preference;

def next_check_index(max, current_index):
    if current_index == (max-1):
        return 0
    return (current_index + 1)

def terms_service(request):
     context = {}
     return render(request, 'terms_service.html',context)

@login_required(login_url='/landing')
def editProfile(request):
    p_form = ProfileUpdateForm()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        birthday = request.POST.get('gender')
        bio = request.POST.get('bio')
        image0 = request.FILES.get('image0')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        p_form.first_name = first_name
        p_form.last_name = last_name
        p_form.city = city
        p_form.gender = gender
        p_form.birthday = birthday
        p_form.bio = bio
        p_form.image0 = image0
        p_form.image1 = image1
        p_form.image2 = image2
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
    myprofile = request.user.userprofile
    matches = myprofile.matches.all()
    context = {'matches': matches}
    return render(request, 'chat.html', context)

@login_required(login_url='/landing')
def chat_room(request, room_name):
    Users = get_user_model()
    myprofile= request.user.userprofile
    c_k = myprofile.current_check
    c_k_user = Users.objects.filter()[(c_k):(c_k + 1)].get()
    myprofile.who_like_me.add(c_k_user)
    n_index = next_check_index(Users.objects.count(), c_k)
    myprofile.current_check = n_index
    myprofile.save()
    match = add_match_if_bothlike(request.user,c_k_user)
    next = Users.objects.filter()[(n_index):(n_index + 1)].get()
    myprofile = request.user.userprofile
    matches = myprofile.matches.all()
    context = {'matches': matches, 'room_name': room_name, 'next': next}
    return render(request,'chat_room.html', context)

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
        gender = request.POST.get('gender_preference')
        relationship = request.POST.get('relationship_preference')
        age_range = request.POST.get('age_range')
        distance = request.POST.get('match_radius')

        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        p_form.gender_preference = gender
        p_form.relationship_preference = relationship
        p_form.age_range = age_range
        p_form.match_radius = distance
        if p_form.is_valid():
            p_form.save()
            return redirect('hunny-preferences')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {'p_form':p_form}
    return render(request, 'preferences_edit.html', context)

@login_required(login_url='/landing')
def settings(request):
    return render(request, 'settings.html')
