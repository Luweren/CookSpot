from django.urls import path
from . import views
from .views import delete_view

app_name = 'web'
urlpatterns = [
    path("users/", views.users, name="users"),
    path("allrecipes/", views.allrecipes, name="allrecipes"),
    path("", views.homepage, name="home"),
    path("homepage/", views.homepage, name="home"),
    path("accounts/login/", views.login, name='login'),
    path("accounts/logout/", views.homepage, name="home"),
    path("signup/", views.signup, name='signup'),
    path("<str:User_username>/newrecipe/", views.newrecipe, name='newrecipe'),
    path('<str:User_username>/recipe/<str:Recipe_name>/',
         views.recipe, name='recipe'),
    path("newrecipe/post/", views.newrecipe_post, name='newrecipe_post'),
    path("signup/post/", views.signup_post, name='signup_post'),
    path("<str:User_username>/myprofile/", views.profile, name="myprofile"),
    path("meets/", views.meets, name="meets"),
    path('<str:User_username>/meet/<str:Meets_name>/', views.meet, name='meet'),
    path('<str:User_username>/meet/<str:Meets_name>/join',
         views.meetjoin, name='meetjoin'),
    path('<str:User_username>/meet/<str:Meets_name>/invite',
         views.meetinvite, name='meetinvite'),
    path('<str:User_username>/meet/<str:Meets_name>/rate/<str:Target_username>',
         views.meetrate, name='rate'),
    path('rate/post', views.meetrate_post, name='rate_post'),
    path('editrate/post', views.editrate_post, name='editrate_post'),
    path('<str:User_username>/newmeet/', views.newmeet, name='newmeet'),
    path('<str:User_username>/mycookgraphy/',
         views.myrecipes, name='mycookgraphy'),
    path('newmeet/post', views.newmeet_post, name='newmeet_post'),
    path('search/', views.search, name="search-things"),
    path('editUserDetails', views.editUserDetails, name="editUserDetails"),
    path("<int:id>/addtofav/<str:ur>", views.add_to_fav, name="addtofav"),
    path('<id>/delete', delete_view, name='delete_fav'),
]
