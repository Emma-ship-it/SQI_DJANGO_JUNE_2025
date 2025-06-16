from django.urls import path
from . import views
app_name='menu'
urlpatterns=[
    path('dish/',views.available_dishes,name='foods')
] 