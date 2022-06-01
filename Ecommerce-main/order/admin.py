from django.contrib import admin

from .models import Order, OrderItem

class OrderControl(admin.ModelAdmin):
    list_display = ('user','paid_amount','created_at','zipcode')

admin.site.register(Order,OrderControl)