from django.contrib import admin
from .views import * 
from django.urls import path,include



urlpatterns =[
    path('',inicio,name='inicio'),
    path('delete/<id>',delete,name='delete'),
    #path('inicio_za/',inicio_za,name='inicio_za'),
    path('inicio_mascaro/',inicio_mascaro,name='inicio_mascaro'),
    path('inicio_masbarato/',inicio_masbarato,name='inicio_masbarato'),
    path('inicio_caracteristicas/',inicio_caracteristicas,name='inicio_caracteristicas'),
    path('inicio_refresh/',inicio_refresh,name='inicio_refresh'),
    path('inicio_propiedades/',inicio_propiedades,name='inicio_propiedades'),
    path('propiedades_za/',propiedades_za,name='propiedades_za'),
    
    #formulario
    path('form_add/',form_add,name='form_add'),
    path('form_edit/<id>',form_edit,name='form_edit'),
    
    
    #direccion

    path('dueño_az/',dueño_az,name='dueño_az'),
    path('dueño_za/',dueño_za,name='dueño_za'),
    
    
    path('direccion_az/',direccion_az,name='direccion_az'),
    path('direccion_za/',direccion_za,name='direccion_za'),
    
    
    path('localidad_za/',localidad_za,name='localidad_za'),
    path('localidad_az/',localidad_az,name='localidad_az'),
    
    
    path('estado_az/',estado_az,name='estado_az'),
    path('estado_za/',estado_za,name='estado_za'),
    
    path('propiedad_az/',propiedad_az,name='propiedad_az'),
    path('propiedad_za/',propiedad_za,name='propiedad_za'),
    
    path('tipo_az/',tipo_az,name='tipo_az'),
    path('tipo_za/',tipo_za,name='tipo_za'),
    
    path('precio_az/',precio_az,name='precio_az'),
    path('precio_za/',precio_za,name='precio_za'),
    
    path('descripcion_az/',descripcion_az,name='descripcion_az'),
    path('descripcion_za/',descripcion_za,name='descripcion_za'),
 

]