from django.urls import path
from urlshortnerapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.reload, name='reload')
]