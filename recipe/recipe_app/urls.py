from django.urls import path
from . import views
app_name= 'recipe_app'
urlpatterns = [
    path('add/recipe/',views.add_recipe, name="recipe_add"),
    # path('recipe/all/',views.recipe_list, name="recipe_list"),
]
