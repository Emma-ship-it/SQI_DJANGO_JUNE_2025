from django.db import models

# Create your models here.
class recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time=models.IntegerField()
    image = models.ImageField( upload_to='recipe_image/', blank = True, null=True)
    cover_image = models.ImageField( upload_to='recipe_image/', blank = True, null=True)
    
    def __str__(self):
        return f"{self.name}"
