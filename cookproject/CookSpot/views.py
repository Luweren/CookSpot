from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import User, Recipe, Ingredients, Meets
# Create your views here.


def homepage(response):
    return render(response, "homepage.html", {})


def users(response):
    return render(response, "users.html", {})


def recipe(response, User_username, Recipe_name):
    user = User.objects.get(username=User_username)
    recipe = user.recipe_set.get(name=Recipe_name)
    if(user != 0 and recipe != 0):
        return render(response, "recipe.html", {'user': user, 'recipe': recipe})


def login(response):
    return render(response, "login.html", {})


def signup(response):
    return render(response, "signup.html", {})


def newrecipe(response, User_username):
    user = User.objects.get(username=User_username)

    return render(response, "newRecipe.html", {'user': user})


def newrecipe_post(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        if(user.recipe_set.get(name=request.POST['recipename']) != 0):
            # placeholder redirect
            return redirect("/homepage")
        recipe = user.recipe_set.create(name=request.POST['recipename'], difficulty=request.POST['difficulty'], tags=request.POST['tags'], description=request.POST['description'],
                                        instructions=request.POST['instructions'], preparationtime=request.POST['preparationtime'], cookingtime=request.POST['cookingtime'], image=request.POST['image'])
        for i in range(len(request.POST.getlist('ingredientname[]'))):
            recipe.ingredients_set.create(name=request.POST.getlist('ingredientname[]')[i], amount=request.POST.getlist(
                'ingredientamount[]')[i]+request.POST.getlist('ingredientmeasurement[]')[i])
        user.save()
        return redirect("/"+request.POST['username']+"/recipe/"+request.POST['recipename'])
    except (KeyError, user.DoesNotExist):
        # placeholder redirect
        return redirect("/"+"homepage")
