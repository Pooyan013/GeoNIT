from django.contrib import admin
from .models import Category

class CartegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CartegoryAdmin)