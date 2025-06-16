from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'demo/index.html')

def about_us(request):
    return render(request,'demo/about-us.html')

def contact(request):
    return render(request,'demo/contact.html')


def menu(request):
    return render(request,'demo/menu.html')
    




