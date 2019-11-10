from django.shortcuts import render, redirect
from django.db import models
from posters.forms import FilteredCategoryForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, SignUp
from django.contrib.auth.mixins import LoginRequiredMixin



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

    def get_queryset(self):
        query = self.request.GET.get("selected")
        print(query)
        if(query is not None):
            return Post.objects.filter(category_tag = query)
        else:
            return Post.objects.all()

#individual page for poster (DOESNT WORK ATM because we didnt handle index shifting in query yet).
class PostDetailView(DetailView):
    model = Post

#stuff for users to create their own posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'content', 'group', 'location', 'date', 'time_start', 'time_end', 'category_tag']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
'''
def signup(request):
    return render(request, 'posters/signup.html', {'title': 'about'})
'''

class SignUpView(CreateView):
    model = SignUp
    fields = ['name', 'email']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def filter_page(request):
    form = FilteredCategoryForm()

    if (request.method == 'POST'):
        form = FilteredCategoryForm(data=request.POST)
        if form.is_valid():
            posters = Post.objects.all()
            selection = form.cleaned_data['selected']
            print(selection)
            #selection = "Activity"
            filtered = Post.objects.filter(category_tag=selection)
            context = {
                'posters': posters,
                'selection': selection,
            }
            return redirect("poster:posters-home", selection)

    return render(request, "posters/filter.html", {'form': form})

