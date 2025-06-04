from django.urls import path
from . import views
urlpatterns = [
    path('community/events/',views.events,name="events")
]
