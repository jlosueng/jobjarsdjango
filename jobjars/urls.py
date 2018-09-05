from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('static/<file>', views.static),
    path('', views.index, name='index'),
]