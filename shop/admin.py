from django.contrib import admin
from .models import Category, Product

class CartegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Category, CartegoryAdmin)
admin.site.register(Product, ProductAdmin)