from django import forms
from .models import recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = "__all__"