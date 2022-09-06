from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['email'],
                                            email=data['email'],
                                            password=data['password_2'])
            user.save()
            return redirect('home:Home')
    else:
        pass