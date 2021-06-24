from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.URLField()
    
    def __str__(self):  
        return self.user.username

#create profile when registering new user
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.URLField()
    #image = models.ImageField(null=True, blank=True, upload_to="images/", height_field=None, width_field=None, max_length=100)
    #properties = models.CharField(max_length=254)
    tags = models.CharField(max_length=254)
    difficulty = models.CharField(max_length=254)
    preparationtime = models.CharField(max_length=254)
    cookingtime = models.CharField(max_length=254)
    instructions = models.TextField()
    
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    amount = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Meets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    date = models.DateField()
    desc = models.TextField()
    def __str__(self):
        return self.name

