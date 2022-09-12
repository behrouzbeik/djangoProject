from django.contrib import admin
from .models import *
# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('EnCaption', 'DeCaption', 'Url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('EnName','DeName', 'create','update')
    prepopulated_fields = {
        'slug' : ('EnName',)
    }

admin.site.register(MenuItems,MenuItemsAdmin)
admin.site.register(Category,CategoryAdmin)







