from django.contrib import admin
from .views import * 
from django.urls import path,include



urlpatterns =[
    path('',inicio,name='inicio'),
    path('delete/<id>',delete,name='delete')
]