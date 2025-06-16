from django.urls import path
from . import views
app_name ='bakery'
urlpatterns = [
    path('',views.home,name='home'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.contact, name='contact_page'),
    path('menu/',views.menu,name='menu_page')
]
