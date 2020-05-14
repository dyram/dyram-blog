from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Dyram',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'August 27,2018'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 2',
        'content': 'second content',
        'date_posted': 'August 28,2018'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
    }
    return render(request, 'blog/about.html', context)
