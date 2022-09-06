from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('en/', views.EnHome, name='Enhome'),
    path('de/', views.DeHome, name='Dehome'),
    path('SeletLanguage/',views.SelectLanguage,name='SelectLanguage'),
]
