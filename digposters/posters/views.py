from django.shortcuts import render
#from django.views.generic import ListView
# from .models import Post
from django.http import HttpResponse

def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return HttpResponse('<h1> Home </h1>')
#    return render(request, 'posters/home.html')

def about(request):
#   return render(request, 'posters/about.html')
    return HttpResponse('<h1> About </h1>')
# class HomePageView(ListView):
#     model = Post
#     template_name = 'home.html'

