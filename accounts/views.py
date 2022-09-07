from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['Email'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:Home')
            else:
                pass
    else:
        pass

    return render(request, 'accounts/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home:Home')