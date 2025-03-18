from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class New(models.Model):
    title = models.CharField(max_length=50, unique=True,verbose_name="عنوان")
    body = models.TextField(verbose_name="متن خبر")
    image = models.ImageField(upload_to='images/News',blank=True ,null=True)
    created = models.DateTimeField(auto_now_add=True,blank=True,verbose_name="تاریخ انتشار")
    updated = models.DateTimeField(auto_now=True,verbose_name="آخرین بروزرسانی")
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(New, self).save(*args, **kwargs)

    def _str_(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Article(models.Model):
    author = models.CharField(max_length=30, verbose_name="نویسنده")
    title = models.CharField(max_length=150, verbose_name="عنوان مقاله")
    slug = models.SlugField(unique=True, blank=True, )
    introduction = models.TextField(verbose_name="مقدمه")
    body = models.TextField(verbose_name="متن مقاله")
    image1 = models.ImageField(upload_to='articles/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='articles/images/', null=True, blank=True)
    pdf = models.FileField(upload_to='articles/pdfs/', verbose_name="فایل PDF", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-created_at']