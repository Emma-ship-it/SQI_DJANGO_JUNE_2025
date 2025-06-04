from django.shortcuts import render,HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('<h1>Welcome to barka street library</h1>')
