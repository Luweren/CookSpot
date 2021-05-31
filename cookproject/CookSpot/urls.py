from django.urls import path
from . import views

urlpatterns=[
    path("users/", views.users, name="users"),
    path("", views.homepage, name="home"),
    path("homepage/", views.homepage, name="home"),
    path('<str:User_username>/<str:Recipe_name>/', views.recipe, name='recipe'),
    path("login/",views.login, name='login'),
    path("signup/",views.signup, name='signup'),
]