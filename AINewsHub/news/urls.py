from Tools.scripts.make_ctype import method
from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('/addLetter', views.addLetter, name='addLetter'),
]