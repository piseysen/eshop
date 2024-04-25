from django.contrib import admin
from .models import Products, Order

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category', 'image']
    
admin.site.register(Products, ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total']
admin.site.register(Order, OrderAdmin)
