from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user
from .models import Recipe, Ingredients, Meets
# Create your views here.

User = get_user_model()


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
    user2 = User.objects.get(username=request.POST['username'])
    try:
        user1 = user2
        rec = Recipe
        try:
            rec = user1.recipe_set.get(name=request.POST['recipename'])
            return redirect("/"+"homepage") 
        except (rec.DoesNotExist):
            recipe = user1.recipe_set.create(name=request.POST['recipename'], difficulty=request.POST['difficulty'], tags=request.POST['tags'], description=request.POST['description'],
                                             instructions=request.POST['instructions'], preparationtime=request.POST['preparationtime'], cookingtime=request.POST['cookingtime'], image=request.POST['image'])
            for i in range(len(request.POST.getlist('ingredientname[]'))):
                recipe.ingredients_set.create(name=request.POST.getlist('ingredientname[]')[i], amount=request.POST.getlist(
                    'ingredientamount[]')[i]+request.POST.getlist('ingredientmeasurement[]')[i])
            user1.save()
            return redirect("/"+request.POST['username']+"/recipe/"+request.POST['recipename'])
    except (KeyError, user2.DoesNotExist):
        # placeholder redirect
        return redirect("/"+"homepage")


def signup_post(request):
    user = User
    try:
        user = User.objects.get(username=request.POST['username'])
        return redirect("/signup")
    except(user.DoesNotExist):
        if(request.POST['password'] != request.POST['rpassword']):
            return redirect("/signup")
        user = User.objects.create_user(
            username=request.POST['username'], email=request.POST['email'], password=request.POST['password'], is_staff=False, is_superuser=False)
        user.save()
        return redirect("/homepage")
        

def profile(response,User_username):
    user = User.objects.get(username=User_username)
    return render(response, "user.html", {'user': user})

def meets(request):
    meets = Meets.objects.filter(user=request.user)
    return render(request, "meets.html", context={'meets': meets})

def meet(response, User_username, Meets_name):
    user = User.objects.get(username=User_username)
    meet = user.meets_set.get(name=Meets_name)
    ingredients = Ingredients.objects.filter(recipe=meet.recipe).order_by("name")
    all_users = User.objects.all()
    if(user != 0 and meet != 0):
        return render(response, "standaloneMeet.html", {'user': user, 'all_users':all_users, 'meet': meet, 'ingredients':ingredients})

def newmeet(response, User_username):
    user = User.objects.get(username=User_username)
    
    return render(response, "newMeet.html", {'user': user})

def newmeet_post(request):
    user2 = User.objects.get(username=request.POST['username'])
    try:
        user1 = user2
        meet = Meets
        try:
            meet = user1.meets_set.get(name=request.POST['meetName'])
            return redirect("/"+"homepage") 
        except (meet.DoesNotExist):
            thisrecipe = user1.recipe_set.get(name=request.POST['recipe'])
            Meet = user1.meets_set.create(name=request.POST['meetName'], recipe=thisrecipe, date=request.POST['meetDate'], desc=request.POST['description'])
            user1.save()
            return redirect("/"+request.POST['username']+"/meet/"+request.POST['meetName'])
    except (KeyError, user2.DoesNotExist):
        # placeholder redirect
        return redirect("/"+"homepage")