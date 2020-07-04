from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    path('<int:pk>/', mainapp.accommodations, name='accommodations'),
]