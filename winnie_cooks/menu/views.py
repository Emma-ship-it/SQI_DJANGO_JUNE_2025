from django.shortcuts import render

# Create your views here.
def available_dishes(request):
    context={
        'name':'stir-fried spag',
        'price' : '$50'
        
    }
    return render(request,'dish/dishes.html',context)
