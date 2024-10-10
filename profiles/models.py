from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    favorite_reptile = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True) 

    def __str__(self):
        return f'{self.user.username} Profile' 

def create_profile(sender, instance, created, **kwargs):  # Define the function here
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User) 