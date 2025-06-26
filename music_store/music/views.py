from django.shortcuts import render,get_object_or_404,redirect
from .models import Artist,Album
from .forms import AlbumForm

# Create your views here.
def home(request):
    return render(request,'music/index.html')

def artist_page(request):
    artist= Artist.objects.order_by('debut_year')
    pictures=  ["beatles.jpeg","coldplay.jpg","taylor.jpeg","adele.jpeg","download.jpeg"]
    # artist_pics=zip(artist,pictures)
    return render(request,'music/artist.html',{"artists" : artist })

def album_page(request):
    artiste=  Artist.objects.all()
    album =  Album.objects.order_by("release_date")
    pictures= ["abbey.jpeg","parachutes.jpeg","21.jpeg","mylo.jpeg","Takecare.jpeg","red.jpeg","taylor.jpeg","Hello.jpeg"]
    # album_pics=zip(album,pictures)
    return render(request, 'music/album.html',{"albums" : album})
def artist_detail(request, artist_pk):
    artist= get_object_or_404(Artist,pk=artist_pk)
    context={'artist' : artist}
    return render(request,'music/artist_detail.html',context)

def album_detail(request, album_pk):
    album= get_object_or_404(Album,pk=album_pk)
    context={'album' : album}
    return render(request,'music/album_detail.html',context)

def create_album(request):
    album_form = AlbumForm()
    if request.method == "POST":
        album_form = AlbumForm(request.POST, request.FILES)
        if album_form.is_valid():
            cleaned_data = album_form.cleaned_data
            Album.objects.create(**cleaned_data) 
            return redirect('music:album')  
    context ={
        "form":album_form
    }  
    return render(request,'music/create_album.html',context)   
        
    