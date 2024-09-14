from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from news.fetch import fetch_ai_newsletter_articles, fetch_youtube_videos
from news.models import Article, Newsletter
import datetime

# Create your views here.
def articles(request):
    articles = Article.objects.order_by('-publication_date')
    if len(articles)== 0 or articles[0].publication_date.date()!=datetime.date.today():
        fetch_ai_newsletter_articles()
        fetch_youtube_videos()
    articles = Article.objects.order_by('-publication_date')
    json = serializers.serialize('json', articles)
    return HttpResponse(json, content_type="application/json")


def addLetter(request):
    newsletter = Newsletter()
    print(request)
    newsletter.title = request.GET['title']
    newsletter.url = request.GET['url']
    newsletter.save()
    return HttpResponse(newsletter.title, content_type="application/json")
