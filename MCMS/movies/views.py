from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

# Create your views here.

def home(request):
    movies= Movie.objects.all()
    return render(request,'movie/index.html',{"movies" : movies})
def movie_detail(request,movie_pk):
    movie= get_object_or_404(Movie,pk=movie_pk)
    return render(request,'movie/movie_det.html',{"movie":movie})

@login_required
def create_movie(request):
    add_movie = MovieForm()
    if request.method == "POST":
        add_movie = MovieForm(request.POST,request.FILES)
        if add_movie.is_valid():
            add_movie.save()
            new_movie = add_movie.save(commit=False)
            new_movie.added_by = request.user
            new_movie.save()
            return redirect('movie:home')
    return render(request,'movie/create_movie.html',{'form':add_movie})   
@login_required 
def update_movie(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES, instance = movie) 
        if form.is_valid():
            form.save()
            return redirect('movie:movie_detail', movie_pk= movie_pk)
    context ={
        'movie':movie,
        'form':form
    }   
    return render(request,'movie/update_movie.html',context)

@login_required
def confirm_delete(request,movie_pk):
    movie = get_object_or_404(Movie,pk = movie_pk)
    return render(request,'movie/confirm_delete.html',{"movie" : movie})

@login_required
def delete_movie(request,movie_pk):
    movie = get_object_or_404(Movie,pk= movie_pk)
    if request.method =="POST":
        movie.delete()
        return redirect('movie:home')
     
    
