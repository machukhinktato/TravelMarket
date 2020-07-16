from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    path('accommodations/<int:pk>/', mainapp.accommodations, name='accommodations'),
    path('accommodation/<int:pk>/', mainapp.accommodation, name='accommodation'),
]