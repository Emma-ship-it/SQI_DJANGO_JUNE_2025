from django.shortcuts import render

# Create your views here.
def practice_dtl(request):
    context={
        'username':'david',
        'no_of_messages':5,
        'messages':['Hello','free to chat ?','When can we talk ?'],
        'is_logged_in':False,
        
    }
    return render(request,'dtl/index.html',context) 
