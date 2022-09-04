from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(MenuItems)





class MenuItems(admin.ModelAdmin):
    list_display = ('EnCaption', 'DeCaption', 'Url')