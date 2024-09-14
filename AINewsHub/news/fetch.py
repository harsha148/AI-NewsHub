from django.utils import timezone
from googleapiclient.discovery import build

from news.models import Article, Newsletter


def fetch_youtube_videos():
    api_key = 'AIzaSyBZOl-uXVm-J1wFqfXDSSB_i_suuiO-_Wo'
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        q='AI News',
        part='snippet',
        type='video',
        maxResults=10
    )
    response = request.execute()
    print(f'Response from youtube: {response}')
    for item in response['items']:
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        video_description = item['snippet']['description']
        # Store in the database
        Article.objects.create(
            title=video_title,
            source='YouTube',
            url=video_url,
            content=video_description,
            publication_date=item['snippet']['publishedAt']
        )


import requests
from bs4 import BeautifulSoup


def fetch_ai_newsletter_articles():
    newsletters = Newsletter.objects.all()
    articles = []
    for newsletter in newsletters:
        url = newsletter.url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles.append(soup.find_all('article')[:5])  # Example limit of 5 articles
    for article in articles:
        title = article[0].find('h2').text
        link = article[0].find('a')['href']
        content = article[0].find('p').text

        # Store in the database
        Article.objects.create(
            title=title,
            source='AI Newsletter',
            url=link,
            content=content,
            publication_date=timezone.now()
        )

