from django import template
import jdatetime
from django.utils.timezone import localtime

register = template.Library()

@register.filter
def to_jalali(value):
    """
    تبدیل تاریخ میلادی به شمسی
    """
    if value:
        try:
            return jdatetime.datetime.fromgregorian(datetime=value).strftime('%Y/%m/%d')
        except ValueError:
            return "تاریخ نامعتبر"
    return ''
