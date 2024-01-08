from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    context = {
        "posts": Post.objects.all(),
        'title': "Home"
    }
    return render(request, "api/home.html", context)

def about(request):
    return render(request, 'api/about.html')
