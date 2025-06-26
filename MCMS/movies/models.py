from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class GenreChoices(models.TextChoices):
        ACTION = 'AC', 'Action'
        DRAMA = 'DR', 'Drama'
        COMEDY = 'CO', 'Comedy'
        HORROR = 'HO', 'Horror'
        ROMANCE = 'RO', 'Romance'
        SCIFI = 'SF', 'Science Fiction'
        FANTASY = 'FA', 'Fantasy'
        DOCUMENTARY = 'DO', 'Documentary'
        THRILLER = 'TH', 'Thriller'


class Movie(models.Model):
        Title = models.CharField(max_length=100)
        Director = models.CharField(max_length=100)
        Release_Date = models.DateField()
        Genre = models.CharField(max_length= 20, choices= GenreChoices.choices,default = GenreChoices.ACTION )
        Description = models.TextField()
        Poster = models.ImageField(upload_to='movie_poster/', blank=True, null= True )
        added_by = models.ForeignKey(User,on_delete=models.CASCADE)
        def __str__(self):
                return f"{self.Title}"
        
