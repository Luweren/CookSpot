from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.
def homepage(response):
    return render(response, "homepage.html",{})
def users(response):
    return render(response, "users.html",{})
