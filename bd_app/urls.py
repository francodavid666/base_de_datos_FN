from django.contrib import admin
from .views import * 
from django.urls import path,include



urlpatterns =[
    path('',inicio,name='inicio'),
    path('delete/<id>',delete,name='delete'),
    path('inicio_za/',inicio_za,name='inicio_za'),
    path('inicio_mascaro/',inicio_mascaro,name='inicio_mascaro'),
    path('inicio_masbarato/',inicio_masbarato,name='inicio_masbarato'),
    path('inicio_caracteristicas/',inicio_caracteristicas,name='inicio_caracteristicas'),
    path('inicio_refresh/',inicio_refresh,name='inicio_refresh'),
]