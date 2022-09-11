from django.contrib import admin
from .models import *
# Register your models here.


class MenuItems(admin.ModelAdmin):
    list_display = ('EnCaption', 'DeCaption', 'Url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update')
    prepopulated_fields = {
        'slug' : ('name',)
    }


admin.site.register(MenuItems)
admin.site.register(Category,CategoryAdmin)
