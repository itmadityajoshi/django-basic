from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_foots  = models.FloatField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    #image 

