from django.shortcuts import render

def editProfile(request):
    return render(request, '../templates/profile.html')