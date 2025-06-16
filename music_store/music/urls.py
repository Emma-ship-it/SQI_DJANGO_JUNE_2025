from django.urls import path
from . import views
app_name = "music"
urlpatterns = [
    path('',views.home,name='home'),
    path('artist/',views.artist_page, name= "artist"),
    path('album/',views.album_page, name = "album")
]
