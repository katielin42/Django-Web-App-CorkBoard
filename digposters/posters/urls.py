<<<<<<< HEAD
=======


>>>>>>> de31b1771c0805e0d3299033a58d256626473d90
from django import urls
from django.urls import path
from . import views
app_name = "poster"

urlpatterns = [
    path('', views.home, name='posters-home'),
    path('about/', views.about, name='posters-about'),
    path('upload/', views.upload_form, name = "upload_form"),
    path('success/', views.success_page, name = "success_page")
]

<<<<<<< HEAD

=======
>>>>>>> de31b1771c0805e0d3299033a58d256626473d90

