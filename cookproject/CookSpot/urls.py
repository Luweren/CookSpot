from django.urls import path
from . import views


app_name = 'web'
urlpatterns=[
    path("users/", views.users, name="users"),
    path("", views.homepage, name="home"),
    path("homepage/", views.homepage, name="home"),
    path("login/",views.login, name='login'),
    path("signup/",views.signup, name='signup'),
    path("<str:User_username>/newrecipe/",views.newrecipe, name='newrecipe'),
    path('<str:User_username>/recipe/<str:Recipe_name>/', views.recipe, name='recipe'),
    path("newrecipe/post/", views.newrecipe_post, name='newrecipe_post'),
    path("signup/post/", views.signup_post, name='signup_post'),
    path("<str:User_username>/myprofile/", views.profile, name="myprofile"),
    path("meets/", views.meets, name="meets"),
    path('<str:User_username>/meet/<str:Meets_name>/', views.meet, name='meet'),
    path('<str:User_username>/newmeet/', views.newmeet, name='newmeet'),
    path('newmeet/post', views.newmeet_post, name='newmeet_post'),
]