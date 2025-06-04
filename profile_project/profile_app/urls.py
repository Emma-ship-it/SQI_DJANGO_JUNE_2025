from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='home'),
    path('hobbies/',views.hobbies,name='hobbies'),
    path('goals/',views.goals,name='goals')
]
