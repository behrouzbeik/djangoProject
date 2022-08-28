from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# Create your views here.

def home(request):
    context = {'title':'Visit Lübeck - QUEEN OF THE HANSEATIC LEAGUE'}
    return render(request,'home/home.html',context)