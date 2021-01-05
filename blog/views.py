from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Blog Home</h1>')


def hi(request):
    return HttpResponse('<p> Hello World</p>')
