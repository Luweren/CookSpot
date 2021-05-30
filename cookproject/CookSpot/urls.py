from django.urls import path
from . import views

urlpatterns=[
    path("users/", views.users, name="users"),
    path("", views.homepage, name="home"),
    path("homepage/", views.homepage, name="home"),
]