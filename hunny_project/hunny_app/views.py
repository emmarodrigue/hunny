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
def matchingroom(request):
    User = get_user_model()
    first = User.objects.filter()[:1].get()
    context = {'first':first}
    return render(request, 'matchingroom.html', context)


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
def like_next(request):
     Users = get_user_model()
     next = Users.objects.filter()[2:3].get()
     profile= request.user.userprofile
     profile.bio = "I have changed!"
     profile.save()
     context = {'next':next, 'current':1}
     return render(request, 'likenext.html',context)

#lilly_note
def dislike_next(request):
     User = get_user_model()
     next = User.objects.filter()[4:5].get()
     context = {'next':next, 'current':1}
     return render(request, 'dislikenext.html',context)


def terms_service(request):
     context = {}
     return render(request, 'terms_service.html',context)

#lilly_note
def accountlogout(request):
    logout(request)
    return redirect('hunny-login')



def home(request):
     return render(request, 'home.html')

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

#lilly_note



@login_required()
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
