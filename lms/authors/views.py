from django.shortcuts import render

# Create your views here.
from .models import Author
from library.models import Book
from django.http import HttpResponse


def all_authors(request):
    return render(request, "author/authors.html")


def book_signings(request):
    return render(request, "author/booksignings.html")


def mvt(request):
    authors = Author.objects.all()
    authors_ordered_by_birth_date = authors.order_by("birth_date")
    books = Book.objects.order_by("-title")
    context = {
        "authors_dob": authors_ordered_by_birth_date,
        "authors": authors,
        "books": books,
    }
    return render(request, "author/mvt.html", context)
