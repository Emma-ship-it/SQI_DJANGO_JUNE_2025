from django.urls import path
from . import views
urlpatterns = [
    path('us/',views.about,name='about_us')
]
