from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import New, Article
import jdatetime


def home(request):
    latest_news = New.objects.all().order_by('-created')[:2]
    latest_articles = Article.objects.all().order_by('-created_at')[:1]

    # تبدیل تاریخ‌ها به شمسی
    for news in latest_news:
        news.created = jdatetime.datetime.fromgregorian(datetime=news.created)

    for article in latest_articles:
        article.created_at = jdatetime.datetime.fromgregorian(datetime=article.created_at)

    return render(request, 'blog/home.html', {'latest_news': latest_news, 'latest_articles': latest_articles})


def geo_news(request):
    news_list = New.objects.all().order_by('-created')
    paginator = Paginator(news_list, 4)
    page_number = request.POST.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/news.html', {'page_obj': page_obj})


def news_detail(request, slug):
    news = get_object_or_404(New, slug=slug)
    return render(request, 'blog/news_detail.html', {'news': news})


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/articles.html", {"page_obj": page_obj})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/articles_detail.html", {"article": article})


def about_us(request):
    return render(request, 'blog/about_us.html')
