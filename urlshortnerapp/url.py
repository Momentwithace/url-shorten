from django.urls import path
from urlshortnerapp import views


urlpatterns = [
    path('', views.index, name='index'),
]