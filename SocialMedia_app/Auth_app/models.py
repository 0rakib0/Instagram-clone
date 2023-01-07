from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
# Create your models here.

class CustomUser(AbstractUser):
    prfole_pic = models.ImageField(upload_to='profile_pic', blank=True)
    cover_pic = models.ImageField(upload_to='profile_pic', blank=True)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    
    
    
class User_More_info(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='more_info')
    work = models.CharField(max_length=200)
    study = models.CharField(max_length=200)
    live_in = models.CharField(max_length=200)
    bio = models.CharField(max_length=260)
    
    
    def __str__(self) -> str:
        return self.user.username
    
class Follow(models.Model):
    Follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower') # Request user follow Other user
    Following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following') # Folloing by request user
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.Following.username + " follwing " + self.Follower.username