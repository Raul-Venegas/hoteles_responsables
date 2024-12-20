from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.hotel_logo.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel_logo = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True , blank=True)
    name_hotel = models.TextField(null=True , blank=True)
    address = models.TextField(null=True, blank=True)
    points_natural = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    points_eco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    points_socio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)