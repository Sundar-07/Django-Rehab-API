from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Create your views here.
def register(request):
    context ={}
    return render(request,'accounts/register.html',context)

def login(request):
    context ={}
    return render(request,'accounts/login.html',context)

def home(request):
    context ={}
    return render(request,'accounts/home.html',context)