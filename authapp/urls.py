from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

url_patterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
]