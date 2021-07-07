from django.contrib import admin
from django.contrib import admin
from .models import Recipe, Meets, Profile, UserRating, Invite, Favourite

# Register your models here.

#admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Meets)
admin.site.register(Profile)
admin.site.register(UserRating)
admin.site.register(Invite)
admin.site.register(Favourite)