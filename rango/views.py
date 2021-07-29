from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

def index(request):
    return HttpResponse("Hello World! <a href='/rango/about/'>About</a>")