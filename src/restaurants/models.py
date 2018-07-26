from django.db import models

# Create your models here.
class RestaurantsLocation(models.Model):
   name = models.CharField(max_length=120)
   location = models.CharField(max_length=120, null=True, blank=True)