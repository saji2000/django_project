from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'blog/home.html')


def hi(request):
    return render(request, 'blog/hi.html')
