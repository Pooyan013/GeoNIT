from django.contrib import admin
from .models import Account
from django_jalali.admin.filters import JDateFieldListFilter
from django.utils.html import format_html

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'full_name', 'phone_number', 'jalali_date_joined', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('jalali_date_joined', 'jalali_last_login')
    list_filter = (
        ('date_joined', JDateFieldListFilter),
        'is_active',
    )

    def jalali_date_joined(self, obj):
        return obj.date_joined.strftime('%Y/%m/%d %H:%M')
    jalali_date_joined.short_description = 'تاریخ عضویت'
    jalali_date_joined.admin_order_field = 'date_joined'

    def jalali_last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime('%Y/%m/%d %H:%M')
        return '-'
    jalali_last_login.short_description = 'آخرین ورود'
    jalali_last_login.admin_order_field = 'last_login'

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'نام کامل'

    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number')
        }),
        ('دسترسی‌ها', {
            'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser')
        }),
        ('تاریخ‌ها', {
            'fields': ('jalali_date_joined', 'jalali_last_login')
        }),
    )

admin.site.register(Account, AccountAdmin)
