from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'base.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile/profile.html')
