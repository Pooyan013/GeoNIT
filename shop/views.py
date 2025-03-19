from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'shop/home.html', context={"products": products}) 
 