from django.shortcuts import render,redirect
from posters.models import Poster
from posters.forms import UploadForm
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

def upload_form(request):
    form = UploadForm()
    if (request.method == 'POST'):
        form = UploadForm(data = request.POST)
        if form.is_valid():
            form.save()
            #return redirect("/success")
            return redirect("poster:success_page")
    return render(request, 'upload_form.html', {'form' : form})
    #return render(request, 'new_post.html', {'form' : form})

def success_page(request):
    print("in success")
    posters_list = Poster.objects.all()
    #print(posters_list[0].description())
    return render(request,'new_post.html', {'poster': posters_list})
