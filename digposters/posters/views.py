from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
#
# #Dummy data just to check shit works
# posts = [
#     {
#         'author': 'URMOM',
#         'title': 'Hacked Poster',
#         'content': 'mike hunt',
#         'date_posted': 'April 20th 2019',
#         'image': 'placeholder',
#     },
#     {
#         'author': 'URMOM',
#         'title': 'Lenna',
#         'content': 'Hugh Janus',
#         'date_posted': 'december 25th 2019',
#         'image': 'placeholder',
#
#     }
#
# ]


#renders the HTML page for home by pulling from the templates folder
def home(request):
    context = {
        'posts': Post.objects.all()
    }     #i changed home.html to base to test out bootstrap.
    return render(request, 'posters/home.html', context)

#renders the HTML page for about by pulling from the templates folder
def about(request):
    return render(request, 'posters/about.html', {'title': 'about'})

#UI of the blog.
class HomePageView(ListView):
    model = Post
    template_name = 'posters/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

#individual page for poster (DOESNT WORK ATM because we didnt handle index shifting in query yet).
class PostDetailView(DetailView):
    model = Post

#stuff for users to create their own posts
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'image', 'content', 'date_posted', 'group']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    