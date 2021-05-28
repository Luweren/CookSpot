from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=254)
    username = models.CharField(max_length=254)
    birthdate = models.DateField()
    email = models.CharField(max_length=254)
    selfdesc = models.TextField()
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    properties = models.CharField(max_length=254)
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
