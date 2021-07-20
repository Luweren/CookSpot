from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields.related import ManyToManyField
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save

# Create your models here.

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.URLField()

    def get_av_rating(self):
        averagescore = 0
        for rating in (self.user.gottenratings.all()):
            averagescore += rating.rating
        try:
            averagescore /= len(self.user.gottenratings.all())
            averagescore = round(averagescore, 2)
        except(ZeroDivisionError):
            averagescore = "No Ratings"
        return averagescore

    def __str__(self):
        return self.user.username


# create profile when registering new user
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
    # image = models.ImageField(null=True, blank=True, upload_to="images/", height_field=None, width_field=None, max_length=100)
    # properties = models.CharField(max_length=254)
    tags = models.CharField(max_length=254)
    difficulty = models.CharField(max_length=254)
    preparationtime = models.CharField(max_length=254)
    cookingtime = models.CharField(max_length=254)
    instructions = models.TextField()
    def __str__(self):
        return self.name


class Ingredients(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, related_name='chosenuser')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    amount = models.CharField(max_length=254)
    measurement = models.CharField(max_length=254)
    def __str__(self):
        return self.name


class Meets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    maximumparticipants = models.IntegerField(blank=True, null=True)
    participants = ManyToManyField(User, related_name="participants", blank=True)
    name = models.CharField(max_length=254)
    date = models.DateField()
    desc = models.TextField()

    def participating(self):
        return len(self.participants.all())

    def __str__(self):
        return self.name


class UserRating(models.Model):
    fromuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='givenratings')
    touser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gottenratings')
    meet = models.ForeignKey(Meets, blank=True, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return str(self.rating) + " by " + str(self.fromuser) + " for " + str(self.touser) + " from " + str(self.meet)

    class META:
        constraints = [
            models.UniqueConstraint(fields=["fromuser", "touser", "meet"], name="1 Rating per Meet")
        ]


class Invite(models.Model):
    fromuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='giveninvites')
    touser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gotteninvites')
    meet = models.ForeignKey(Meets, on_delete=models.CASCADE)

    def __str__(self):
        return "Invite by " + str(self.fromuser) + " to " + str(self.touser) + " for " + str(self.meet) + " on " + str(
            self.meet.date)


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    cookfav = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favcook', null=True, blank=True)