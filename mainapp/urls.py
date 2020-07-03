from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('products/', mainapp.accommodations, name='products'),
]