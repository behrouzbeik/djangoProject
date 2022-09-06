from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from accounts.forms import UserRegisterForm,UserLoginForm


# Create your views here.

def Home(request):
    return redirect('home:Enhome')

def EnHome(request):
    menu_items = MenuItems.objects.all()
    userregisterform = UserRegisterForm()
    userloginform = UserLoginForm()
    context = {
        'title': 'QUEEN OF THE TURISM',
        'Lang': 'De',
        'SignIn':'Sign In',
        'SignOut':'SignOut',
        'SignUp':'SignUp',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu',
        'menu_items': menu_items,
        'Airplane':'Airplane',
        'Train' : 'Train',
        'userregisterform' : userregisterform,
        'userloginform' : userloginform
    }
    return render(request, 'home/EnHome.html', context)

def DeHome(request):
    menu_items = MenuItems.objects.all()
    userregisterform = UserRegisterForm()
    userloginform = UserLoginForm()
    context = {
        'title': 'KÖNIGIN DES TOURISMUS',
        'Lang': 'En',
        'SignIn': 'Einloggen',
        'SignOut': 'austragen',
        'SignUp': 'Anmelden',
        'Search': 'Suche',
        'Services': 'Dienstleistungen',
        'Menu': 'Menü',
        'menu_items':menu_items,
        'Airplane' : 'Flugzeug',
        'Train' : 'Zug',
        'userregisterform': userregisterform,
        'userloginform': userloginform
    }
    return render(request, 'home/EnHome.html', context)

def SelectLanguage(request):
    pass