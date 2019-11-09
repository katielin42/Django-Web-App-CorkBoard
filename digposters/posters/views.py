from django.shortcuts import render
#from django.views.generic import ListView
# from .models import Post

def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'posters/home.html')

def about(request):
    return render(request, 'posters/about.html')
# Create your views here.

# class HomePageView(ListView):
#     model = Post
#     template_name = 'home.html'

