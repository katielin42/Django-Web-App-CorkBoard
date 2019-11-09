'''
from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='posters-home'),
    path('about/', views.about, name='posters-about'),
]

'''

