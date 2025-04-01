from django.db import models
from django.urls import reverse
from accounts.models import Account


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True, default="بدون توضیحات")
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        ordering = ['-category_name']
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True, verbose_name="نام محصول")
    slug = models.SlugField(max_length=200, unique=True)
    product_description = models.TextField(max_length=255, blank=True, default="بدون توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return f"{self.product_name} ({self.category.category_name})"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="carts")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"
