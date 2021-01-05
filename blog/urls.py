from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('hi/', views.hi, name='blog-hi'),
]
