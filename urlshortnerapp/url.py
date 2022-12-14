from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

from urlshortnerapp.views import index

urlpatterns = [
    path('home/', index),

    ]