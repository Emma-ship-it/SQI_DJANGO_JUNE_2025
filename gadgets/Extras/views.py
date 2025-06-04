from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
    return HttpResponse('<div>We sell several gadgets </div>')