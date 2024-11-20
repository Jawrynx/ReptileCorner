from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reptile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reptiles')
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    species = models.CharField(max_length=70)
    bio = models.TextField()
    reptile_picture = models.ImageField(upload_to='reptile_pics/', blank=True)

    def __str__(self):
        return f'{self.user.username} Reptile'
