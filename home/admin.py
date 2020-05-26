from django.contrib import admin
from .models import Product, Cart
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'name', 'date', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    search_fields = ('name', 'date', 'price', 'category')
    # list_per_page = 10
    
admin.site.register(Product, ProductAdmin)
   
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_owned')
    list_filter = ('user',)
    search_fields = ('product', 'user')
    list_display_links = ('user', 'is_owned')
admin.site.register(Cart, CartAdmin)
