from django.contrib import admin
from django.utils.html import format_html
from .models import New , Article

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    list_filter = ('created',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at", "article_preview")
    list_filter = ("created_at", "updated_at", "author")
    search_fields = ("title", "author", "introduction")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    def article_preview(self, obj):

        if obj.image1:
            return format_html('<img src="{}" width="70" height="50" style="object-fit: cover;"/>', obj.image1.url)
        return "بدون تصویر"

    article_preview.short_description = "پیش‌نمایش"