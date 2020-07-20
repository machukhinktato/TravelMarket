import adminapp.views as adminapp
from django.urls import path


app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('countries/create/', adminapp.country_create, name='country_create'),
    path('countries/read/', adminapp.countries, name='countries'),
    path('countries/update/<int:pk>/', adminapp.country_update, name='country_update'),
    path('countries/delete/<int:pk>/', adminapp.country_delete, name='country_delete'),
    path('accommodation/create/countries/<int:pk>/', adminapp.accommodation_create, name='accommodation_create'),
    path('accommodation/read/countries/<int:pk>/', adminapp.accommodations, name='accommodations'),
    path('accommodation/read/<int:pk>/', adminapp.accommodation_read, name='accommodation_read'),
    path('accommodation/update/<int:pk>/', adminapp.accommodation_update, name='accommodation_update'),
    path('accommodation/delete/<int:pk>/', adminapp.accommodation_delete, name='accommodation_delete'),
]
