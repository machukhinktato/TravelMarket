from django.contrib import admin
from django.urls import path
from .views import mainapp

urlpatterns = [
    path('', mainapp),
]