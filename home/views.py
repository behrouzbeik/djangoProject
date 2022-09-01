from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# Create your views here.

def Home(request):
    context = {
        'title': 'QUEEN OF THE TURISM',
        'Lang': 'De',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu'
    }
    return render(request, 'home/EnHome.html', context)

def EnHome(request):
    context = {
                'title':'QUEEN OF THE TURISM',
                'Lang':'De',
                'Search':'Search',
                'Services':'Services',
                'Menu':'Menu'
              }
    return render(request,'home/EnHome.html',context)


def DeHome(request):
    context = {
        'title': 'KÖNIGIN DES TOURISMUS',
        'Lang': 'En',
        'Search': 'Suche',
        'Services': 'Dienstleistungen',
        'Menu': 'Menü'
    }
    return render(request, 'home/EnHome.html', context)

def SelectLanguage(request):
    pass