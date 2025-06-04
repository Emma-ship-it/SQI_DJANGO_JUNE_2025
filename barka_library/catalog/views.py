from django.shortcuts import render,HttpResponse

# Create your views here.
def books(request):
    return HttpResponse("""
       <ul>
          <li>Things fall apart</li>
          <li>The hungry lion</li>
          <li>The lion and the tail</li>
          <li>Rise of apes</li>
          <li>The gods are crazy</li>
       </ul>                 
                        """)
def special(request):
    return HttpResponse("""
                        
     <div>
        <ul>
          <li>Things fall apart</li>
          <li>The hungry lion</li>
       </ul>  
     </div>               
                        """)    
    
