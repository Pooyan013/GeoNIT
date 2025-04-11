from django.urls import path
from .views import home, geo_news, news_detail, article_list, article_detail,about_us

urlpatterns = [
    path('', home, name='home'),
    path('geo-news/', geo_news, name='geo_news'),
    path('news_detail/<slug:slug>/', news_detail, name='news_detail'),
    path("articles/", article_list, name="article"),
    path("articles_detail/<slug:slug>/", article_detail, name="article_detail"),
    path('about_us/', about_us, name='about_us'),

]
