from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.Register, name='Register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout')
]
