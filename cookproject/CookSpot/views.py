from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user
import numpy.random as rand
import datetime
from .models import Recipe, Ingredients, Meets, Profile, UserRating, Favourite

# Create your views here.

User = get_user_model()
today = datetime.date.today()


def homepage(response):
    recipe = Recipe.objects.all()[rand.randint(0, len(Recipe.objects.all()))]
    meets = []
    for x in range(0, 5):
        day = (today + datetime.timedelta(days=x))
        for meet in Meets.objects.all():
            if meet.date == day:
                meets.append(meet)
    return render(response, "homepage.html", {'recipe': recipe, 'meets': meets})


@login_required()
def users(request):
    users = User.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searchedUsers = User.objects.filter(username__contains=searched)
        return render(request, "users.html", {'searched': searched, 'users': searchedUsers})
    # return render(request, "users.html", {})

    return render(request, "users.html", {'users': users})


@login_required()
def myrecipes(response, User_username):
    user = User.objects.get(username=User_username)
    return render(response, "userrecipes.html", {'user': user})


@login_required()
def allrecipes(response):
    recipes = Recipe.objects.all()
    return render(response, "all_recipes.html", {'recipes': recipes})


@login_required()
def recipe(response, User_username, Recipe_name):
    user = User.objects.get(username=User_username)
    recipe = user.recipe_set.get(name=Recipe_name)
    if (user != 0 and recipe != 0):
        return render(response, "recipe.html", {'user': user, 'recipe': recipe})


def login(response):
    return render(response, "homepage.html", {})


"""def login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect("/"+"homepage")
        else:
            # Redirect to login page
            return redirect("/"+"login")
    else:
        # Redirect to login page
        return redirect("/"+"login")"""


def signup(response):
    return render(response, "signup.html", {})


@login_required()
def newrecipe(response, User_username):
    user = User.objects.get(username=User_username)
    return render(response, "newRecipe.html", {'user': user})


@login_required()
def newrecipe_post(request):
    user2 = User.objects.get(username=request.POST['username'])
    try:
        user1 = user2
        rec = Recipe
        try:
            rec = user1.recipe_set.get(name=request.POST['recipename'])
            return redirect("/" + "homepage")
        except (rec.DoesNotExist):
            recipe = user1.recipe_set.create(name=request.POST['recipename'], difficulty=request.POST['difficulty'],
                                             tags=request.POST['tags'], description=request.POST['description'],
                                             instructions=request.POST['instructions'],
                                             preparationtime=request.POST['preparationtime'],
                                             cookingtime=request.POST['cookingtime'], image=request.POST['image'])
            for i in range(len(request.POST.getlist('ingredientname[]'))):
                recipe.ingredients_set.create(name=request.POST.getlist('ingredientname[]')[i],
                                              amount=request.POST.getlist('ingredientamount[]')[i],
                                              measurement = request.POST.getlist('ingredientmeasurement[]')[i])
            user1.save()
            return redirect("/" + request.POST['username'] + "/recipe/" + request.POST['recipename'])
    except (KeyError, user2.DoesNotExist):
        # placeholder redirect
        return redirect("/" + "homepage")


def signup_post(request):
    user = User
    try:
        user = User.objects.get(username=request.POST['username'])
        return redirect("/signup")
    except(user.DoesNotExist):
        if (request.POST['password'] != request.POST['rpassword']):
            return redirect("/signup")
        user = User.objects.create_user(
            username=request.POST['username'], email=request.POST['email'], password=request.POST['password'],
            is_staff=False, is_superuser=False)
        user.save()
        return redirect("/homepage")


@login_required()
def profile(request, User_username):
    user = User.objects.get(username=User_username)
    loggedin = request.user
    fav_list = Favourite.objects.filter(user=user)
    return render(request, "user.html", {'user': user, 'loggedin': loggedin, 'fav_list': fav_list})


@login_required()
def add_to_fav(request, id, ur):
    user = request.user
    if ur == 'rec':
        recipe = Recipe.objects.get(id=id)
        Favourite.objects.get_or_create(user=user, recipe=recipe)
    if ur == 'cook':
        cook = User.objects.get(id=id)
        Favourite.objects.get_or_create(user=user, cookfav=cook)
    return redirect('/')


@login_required()
def delete_view(request, id):
    obj = get_object_or_404(Favourite, id=id)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def recipe_delete(request, rec_id):
    recipe = Recipe.objects.get(id = rec_id)
    obj = get_object_or_404(Recipe, id=rec_id)
    obj.delete()
    return render(request, "userrecipes.html", context={'user': request.user})

@login_required()
def meet_delete(request, meet_id):
    meet = Meets.objects.get(id = meet_id)
    obj = get_object_or_404(Meets, id=meet_id)
    obj.delete()
    return render(request, "meets.html", context={'meets': Meets.objects.all()})

@login_required()
def meets(request):
    meets = Meets.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searchedMeats = Meets.objects.filter(name__contains=searched)
        return render(request, "meets.html", {'searched': searched, 'meats': searchedMeats})
    # return render(request, "meets.html", {})

    return render(request, "meets.html", context={'meets': meets})


@login_required()
def meet(request, User_username, Meets_name):
    user = User.objects.get(username=User_username)
    meet = user.meets_set.get(name=Meets_name)
    meet.participants.add(user)
    ingredients = Ingredients.objects.filter(
        recipe=meet.recipe).order_by("name")
    all_users = User.objects.all()
    if request.method == "POST":
        invited = User.objects.get(username=request.POST['invited'])
        meet.participants.add(invited)
    if (user != 0 and meet != 0):
        return render(request, "standaloneMeet.html",
                      {'user': user, 'all_users': all_users, 'meet': meet, 'ingredients': ingredients})


@login_required()
def meetjoin(request, User_username, Meets_name):
    user = User.objects.get(username=User_username)
    meet = user.meets_set.get(name=Meets_name)
    meet.participants.add(request.user)
    return redirect("/" + User_username + "/meet/" + Meets_name + "/")


@login_required()
def meetinvite(request, User_username, Meets_name):
    owner = User.objects.get(username=User_username)
    meet = owner.meets_set.get(name=Meets_name)
    givenratings = request.user.givenratings.all()
    givenusers = []
    scores = []
    x = givenratings.all().values('touser').distinct()
    for rating in givenratings:
        if rating.touser.username not in givenusers:
            givenusers.append(rating.touser.username)
    for user in givenusers:
        score = 0
        counter = 0
        for rating in givenratings:
            if rating.touser.username == user:
                score += rating.rating
                counter += 1
        score /= counter
        scores.append(score)
    userandscore = list(zip(scores, givenusers))
    userandscore.sort(reverse=True)
    if request.method == "POST":
        searched = request.POST['searched']
        users = User.objects.filter(username__contains=searched)
        return render(request, "invite.html", {'owner': owner, 'meet': meet, 'givenscores': userandscore, 'allusers': User.objects.all(), 'searched': searched, 'searched_users': users})
    return render(request, "invite.html", {'owner': owner, 'meet': meet, 'givenscores': userandscore, 'allusers': User.objects.all().exclude(username = owner.username)})

@login_required()
def meetrate(request, User_username, Meets_name, Target_username):
    user = User.objects.get(username=User_username)
    meet = user.meets_set.get(name=Meets_name)
    target = User.objects.get(username=Target_username)
    try:
        rating = user.givenratings.get(fromuser=user, touser=target, meet=meet)
        return render(request, "editrate.html", {'user': user, 'target': target, 'meet': meet, 'rating': rating})

    except(UserRating.DoesNotExist):
        return render(request, "rate.html", {'user': user, 'target': target, 'meet': meet})


@login_required()
def meetrate_post(request):
    user = User.objects.get(username=request.POST['cuser'])
    target = User.objects.get(username=request.POST['target'])
    meet = Meets.objects.get(name=request.POST['meet'])
    user.givenratings.create(fromuser=user, touser=target,
                             meet=meet, rating=request.POST['rating'])
    user.save()
    return redirect("/" + meet.user.username + "/meet/" + meet.name + "/")


def editrate_post(request):
    user = User.objects.get(username=request.POST['cuser'])
    target = User.objects.get(username=request.POST['target'])
    meet = Meets.objects.get(name=request.POST['meet'])
    rating = user.givenratings.get(fromuser=user, touser=target, meet=meet)
    rating.rating = request.POST['rating']
    rating.save()
    return redirect("/" + meet.user.username + "/meet/" + meet.name + "/")


@login_required()
def newmeet(response, User_username):
    user = User.objects.get(username=User_username)

    return render(response, "newMeet.html", {'user': user})


@login_required()
def newmeet_post(request):
    user2 = User.objects.get(username=request.POST['username'])
    try:
        user1 = user2
        meet = Meets
        try:
            meet = user1.meets_set.get(name=request.POST['meetName'])
            return redirect("/" + "homepage")
        except (meet.DoesNotExist):
            thisrecipe = user1.recipe_set.get(name=request.POST['recipe'])
            Meet = user1.meets_set.create(name=request.POST['meetName'], maximumparticipants=request.POST['pnumber'],
                                          recipe=thisrecipe, date=request.POST['meetDate'],
                                          desc=request.POST['description'], location=request.POST['location'])
            Meet.participants.add(user1)
            user1.save()
            return redirect("/" + request.POST['username'] + "/meet/" + request.POST['meetName'])
    except (KeyError, user2.DoesNotExist):
        # placeholder redirect
        return redirect("/" + "homepage")


# @login_required() ?
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(tags__contains=searched)
        names = Recipe.objects.filter(name__contains=searched)
        return render(request, "search.html", {'searched': searched, 'recipes': recipes, 'names': names})
    return render(request, "search.html", {})


@login_required()
def editUserDetails(request):
    user = request.user
    # user.refresh_from_db()
    if request.method == "POST":
        if (request.POST['username']):
            user.username = request.POST['username']
        if (request.POST['firstName']):
            user.first_name = request.POST['firstName']
        if (request.POST['lastName']):
            user.last_name = request.POST['lastName']
        if (request.POST['email']):
            user.email = request.POST['email']
        if (request.POST['bio']):
            user.profile.bio = request.POST['bio']
        if (request.POST['image']):
            user.profile.profile_photo = request.POST['image']
        user.save()
        return render(request, "user.html", {'user': user})
    return render(request, "user.html", {'user': user})

@login_required()
def edit_recipe(request, Recipe_name):
    recipe = Recipe.objects.get(name = Recipe_name)
    return render(request, "editRecipe.html", {'recipe': recipe})

@login_required()
def edit_recipe_post(request, Recipe_name):
    recipe = Recipe.objects.get(name = Recipe_name)
    if request.method == "POST":
        if (request.POST['recipename']):
            recipe.name = request.POST['recipename']
        if (request.POST['description']):
            recipe.description = request.POST['description']
        if (request.POST['tags']):
            recipe.tags = request.POST['tags']
        if (request.POST['difficulty']):
            recipe.difficulty = request.POST['difficulty']
        if (request.POST['preparationtime']):
            recipe.preparationtime = request.POST['preparationtime']
        if (request.POST['cookingtime']):
            recipe.cookingtime = request.POST['cookingtime']
        if (request.POST['image']):
            recipe.image = request.POST['image']
        if (request.POST['instructions']):
            recipe.instructions = request.POST['instructions']
        
        length = len(request.POST.getlist('ingredientname[]'))
        for i in range(length):
            if len(recipe.ingredients_set.all())!=0:
                recipe.ingredients_set.all()[0].delete()
        

        for i in range(len(request.POST.getlist('ingredientname[]'))):
            if request.POST.getlist('ingredientname[]')[i] != '':
                recipe.ingredients_set.create(name=request.POST.getlist('ingredientname[]')[i],
                amount=request.POST.getlist('ingredientamount[]')[i],
                            measurement=request.POST.getlist('ingredientmeasurement[]')[i])
        

        recipe.save()

        return render(request, "recipe.html", {'recipe': recipe})
    return render(request, "recipe.html", {'recipe': recipe})

@login_required()
def edit_meet(request, Meet_name):
    meet = Meets.objects.get(name = Meet_name)
    return render(request, "editMeet.html", {'meet': meet})

@login_required()
def edit_meet_post(request, Meet_name):
    meet = Meets.objects.get(name = Meet_name)
    if request.method == "POST":
        if (request.POST['meetName']):
            meet.name = request.POST['meetName']
        if (request.POST['meetDate']):
            meet.date = request.POST['meetDate']
        if (request.POST['description']):
            meet.desc = request.POST['description']
        if (request.POST['pnumber']):
            meet.maximumparticipants = request.POST['pnumber']
        meet.save()
        return render(request, "meets.html", {'meets': Meets.objects.all()})
    return render(request, "meets.html", {'meets': Meets.objects.all()})

@login_required()
def uninvite(request, Meets_name, User_username):
    toUninvite = User.objects.get(username=User_username)
    meet = Meets.objects.get(name = Meets_name)
    meet.participants.remove(toUninvite)
    return render(request, "standaloneMeet.html", {'meet': meet})
