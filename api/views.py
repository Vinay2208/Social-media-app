from django.shortcuts import render


# Create your views here.

posts = [
    {"author": "Author1",
     "title": "Post1",
     "content": "This is my first post!"},
    {"author": "Author2",
     "title": "Post2",
     "content": "This is my second post!"},
    {"author": "Author3",
     "title": "Post3",
     "content": "This is my third post!"}
]


def members(request):
    context = {
        "posts": posts,
        'title': "Latest Posts"
    }
    return render(request, "api/home.html", context)

