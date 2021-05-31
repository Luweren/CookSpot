from django.urls import path
from . import views

urlpatterns=[
    path("users/", views.users, name="users"),
    path("", views.homepage, name="home"),
    path("homepage/", views.homepage, name="home"),
    path("recipe/", views.recipe, name="recipe"),
    path('<str:User_username>/<str:Recipe_name>/', views.recipe, name='recipe'),
    path('<User_name>', views.recipe, name='recipe2'),
]