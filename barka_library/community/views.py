from django.shortcuts import render,HttpResponse

# Create your views here.
def events(request):
    return HttpResponse('<section>Novel exhibition coming up on 15/27/2025</section>')
