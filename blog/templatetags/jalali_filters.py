from django import template
import jdatetime
from django.utils.timezone import localtime

register = template.Library()

@register.filter
def to_jalali(value):
    if not value:
        return ""
    value = localtime(value) 
    jalali_date = jdatetime.datetime.fromgregorian(datetime=value)
    return jalali_date.strftime("%Y/%m/%d - %H:%M")
