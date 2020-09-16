from django.contrib import admin
from django.urls import path

from HelloVue import views

urlpatterns = [
    path('', views.index),
]
