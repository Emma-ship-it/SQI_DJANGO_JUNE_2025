from django.shortcuts import render,HttpResponse

# Create your views here.
def gadgets(request):
    return HttpResponse("""
    <ol>
    <li>Laptops</li>
    <li>Phones</li>
    <li>chargers</li>
    <li>Mifi</li>
    </ol> 
                        """)