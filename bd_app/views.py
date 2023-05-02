from django.shortcuts import render
from .models import *
from django import forms
# Create your views here.


def inicio (request):
    
    form = dueño_model.objects.all()
    form2 = datos_propiedad_model.objects.all()
    return render (request,'bd_app/inicio.html',{'form':form,'form2':form2})
