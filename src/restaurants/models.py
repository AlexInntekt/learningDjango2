from django.db import models

# Create your models here.
class RestaurantsLocation(models.Model):
   name          = models.CharField(max_length=120)
   location      = models.CharField(max_length=120, null=True, blank=True)
   
   category      = models.CharField(max_length=120, null=True, blank=True)
   time_stamp    = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
   updated       = models.DateTimeField(auto_now=True)
   #my_date_field = models.DateField(auto_now=False, auto_now_add=False)

   
   
   
   
   
   
   
   
   
   