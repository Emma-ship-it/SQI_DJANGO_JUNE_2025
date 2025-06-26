from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone



def validate_release_date(release_date):
    current_year = timezone.now().year
    if release_date.year not in range(1800,current_year+1):
        raise ValidationError(f"Release date from between year 1800 and {current_year}")
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50, validators = [MinLengthValidator(2)])
    debut_year = models.PositiveIntegerField()
    image= models.ImageField(upload_to ='artist_image/',blank=True,null=True)
    
    def __str__(self):
        return f"{self.name}"

class Album(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(validators = [validate_release_date])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image=  models.ImageField(upload_to = 'album_image/',blank = True, null = True)
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
