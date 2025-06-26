from django import forms
from .models import Artist,Album

class AlbumForm(forms.Form):
    title = forms.CharField(max_length=50)
    release_date = forms.DateField()
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    image=  forms.ImageField(required=False)