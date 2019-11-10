from django.shortcuts import render,redirect
from posters.models import Poster
from posters.forms import UploadForm, FilteredCategoryForm
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

def filter_page(request):
    form = FilteredCategoryForm()
    if (request.method == 'POST'):
        form = FilteredCategoryForm(data = request.POST)
        if form.is_valid():
            #form.save()
            posters = Poster.objects.all()
            selection = form.cleaned_data['selected']
            print(selection)

            #filtered = Poster.objects.get(category_tag = 'Activity')
            #filtered = Poster.objects.all().values_list('username', flat=True)
            filtered = Poster.objects.filter(category_tag = selection)
            #print(filtered.length)
            context = {
                'posters': posters,
                'selection': selection,
            }

            #return redirect("poster:success_page")
            #return redirect("/success")
            return render(request, "filtered_content.html", {"filtered": filtered})

    return render(request, "filter.html", {'form' : form})

