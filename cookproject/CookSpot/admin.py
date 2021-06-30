from django.contrib import admin
from django.contrib import admin
from .models import Recipe, Meets, Profile, UserRating
# Register your models here.

#admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Meets)
admin.site.register(Profile)
admin.site.register(UserRating)