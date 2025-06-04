from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def all_authors(request):
    return render(request,'author/authors.html')

def book_signings(request):
    return render(request,'author/booksignings.html')