from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import recipe

# Create your views here.
def add_recipe(request):
    create_recipe = RecipeForm()
    if request.method == "POST":
        create_recipe = RecipeForm(request.POST, request.FILES)
        if create_recipe.is_valid():
            create_recipe.save()
            # return redirect('recipe_app:recipe_list')
    context={
        "create_recipe":create_recipe
    }  
    return render(request,"add_recipe.html",context)  
