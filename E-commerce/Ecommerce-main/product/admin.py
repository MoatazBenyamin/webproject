from itertools import product
from msilib import add_tables
from django.contrib import admin

from .models import Product , Category
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)


class OrderControl(admin.ModelAdmin):
    list_display = ('name','category','description','price','date_added')

admin.site.register(Product,OrderControl)

class CategoryControl(admin.ModelAdmin):
    list_display = ('name','slug')

admin.site.register(Category,CategoryControl)

admin.site.site_header = "Greatest Watches"
admin.site.site_title = "Admin Panel"

