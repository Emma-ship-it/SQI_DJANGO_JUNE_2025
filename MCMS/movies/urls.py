from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    path('',views.home, name = "home"),
    path('movie/<int:movie_pk>',views.movie_detail, name = "movie_detail"),
    path('add/movie',views.create_movie,name= 'add'),
    path('update/movie/<int:movie_pk>',views.update_movie, name = "edit"),
    path('confirm/movie/<int:movie_pk>',views.confirm_delete,name='confirm_delete'),
    path('delete/movie/<int:movie_pk>',views.delete_movie,name = "delete_movie")
    
]
