from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'last_login', 'date_joined', 'is_admin', 'is_staff')
    list_display_links = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    search_fields = ('email', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
