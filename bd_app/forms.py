from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings


class datos_propiedad_form(forms.ModelForm):

    class META: 
        model= datos_propiedad_model
        fields= '__all__'