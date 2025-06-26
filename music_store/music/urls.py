from django.urls import path
from . import views
app_name = "music"
urlpatterns = [
    path('',views.home,name='home'),
    path('artist/',views.artist_page, name= "artist"),
    path('album/',views.album_page, name = "album"),
    path('author/<int:artist_pk>',views.artist_detail,name = "artist_detail"),
    path('album/<int:album_pk>',views.album_detail,name = "album_detail"),
    path('add/album/',views.create_album, name = "create_album")
]
