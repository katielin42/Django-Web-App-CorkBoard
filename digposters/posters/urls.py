from django.urls import path
from . import views
from .views import HomePageView, PostDetailView, PostCreateView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='posters-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='posters-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
