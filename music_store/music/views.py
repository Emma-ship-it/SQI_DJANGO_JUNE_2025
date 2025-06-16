from django.shortcuts import render
from .models import Artist,Album

# Create your views here.
def home(request):
    return render(request,'music/index.html')

def artist_page(request):
    artist= Artist.objects.order_by('debut_year')
    pictures=  ["beatles.jpeg","coldplay.jpg","taylor.jpeg","adele.jpeg","download.jpeg"]
    artist_pics=zip(artist,pictures)
    return render(request,'music/artist.html',{"artists" : artist_pics })

def album_page(request):
    artiste=  Artist.objects.all()
    album =  Album.objects.order_by("release_date")
    pictures= ["abbey.jpeg","parachutes.jpeg","21.jpeg","mylo.jpeg","Takecare.jpeg","red.jpeg","taylor.jpeg","Hello.jpeg"]
    album_pics=zip(album,pictures)
    return render(request, 'music/album.html',{"albums" : album_pics})
    