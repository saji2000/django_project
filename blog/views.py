from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sajad',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'January 5, 2021',
    },
    {
        'author': 'Hasan',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': 'January 6, 2021',
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def hi(request):
    return render(request, 'blog/about.html', {'title': 'About'})
