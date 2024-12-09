from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel_logo = models.ImageField(upload_to="profiles", null=True, blank=True)
    bio = models.TextField(null=True , blank=True)
    address = models.TextField(null=True, blank=True)
    points_natural = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False) 
    points_eco = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False) 
    points_socio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False) 