from . import views
from .views import HomePageView, PostDetailView, PostCreateView
from django import urls
from django.urls import path
app_name = "poster"

urlpatterns = [
    path('', HomePageView.as_view(), name='posters-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='posters-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('upload/', views.upload_form, name = "upload_form"),
    path('success/', views.success_page, name = "success_page")
]



]
