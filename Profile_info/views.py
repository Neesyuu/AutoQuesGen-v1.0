from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profileView(request):
    return render(request, 'profile/profile.html')

@login_required
def editProfile(request):
    return HttpResponse('Edit profile')
