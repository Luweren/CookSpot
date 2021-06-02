from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import User, Recipe, Ingredients, Meets
# Create your views here.
def homepage(response):
    return render(response, "homepage.html",{})
def users(response):
    return render(response, "users.html",{})
def recipe(response,User_username,Recipe_name):
    user = User.objects.get(username=User_username)
    recipe = user.recipe_set.get(name=Recipe_name)
    if(user != 0):
        if(recipe != 0):
            return render(response, "recipe.html",{'user':user, 'recipe':recipe})
def login(response):
    return render(response, "login.html",{})   
def signup(response):
    return render(response, "signup.html",{})   
def newrecipe(response, User_username):
    user = User.objects.get(username=User_username)

    return render(response, "newRecipe.html",{})   