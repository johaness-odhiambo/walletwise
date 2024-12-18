from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    active_status = models.BooleanField(default=False)
    
    def __str__(self):
         return self.user.username

