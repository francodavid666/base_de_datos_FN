from django.shortcuts import render,redirect

from .models import *
from django import forms
from django.db.models import Q
# Create your views here.


def inicio (request):
    queryset = request.GET.get('buscar')
   # clientes= datos_propiedad_model.objects.all()
   
    clientes = datos_propiedad_model.objects.all()
    clientes= datos_propiedad_model.objects.filter(dueño = True)
    if queryset:
        clientes= datos_propiedad_model.objects.filter(
          Q(tipo__icontains = queryset) |
          Q(direccion__icontains = queryset) |
          Q(localidad__icontains = queryset) |
          Q(tipo__icontains = queryset) |
          Q(precio__icontains = queryset) |
          Q(tipo__icontains = queryset) |
          Q(dueño__icontains = queryset)
        ).distinct()
    
    
    
    #form = dueño_model.objects.all()
    #form2 = datos_propiedad_model.objects.all()
    return render (request,'bd_app/inicio.html',{'clientes':clientes})




def edit(request):
  propiedad= datos_propiedad_model.get(id=id)
  if request.method == 'POST':
    
    form = datos_propiedad_form(request.POST)
    if form.is_valid():
      info = form.cleaned_data
      
      propiedad.dueño=info['dueño']
      propiedad.tipo=info['tipo']
      propiedad.estado=info['estado']
      propiedad.pais=info['pais']
      propiedad.provincia=info['provincia']
      propiedad.localidado=info['localidad']
      propiedad.parcela=info['parcela']
      propiedad.lote=info['lote']
      propiedad.tamaño=info['tamaño']
      propiedad.metros2=info['metros2']
      propiedad.clave=info['clave']
      
      
      propiedad.titular=info['titular']
      propiedad.propiedad=info['propiedad']
      propiedad.ambientes=info['ambientes']
      propiedad.baños=info['baños']
      propiedad.dormitorios=info['dormitorios']
      propiedad.cocina=info['cocina']
      propiedad.living=info['comedor']
      propiedad.garage=info['garage']
      propiedad.sotano=info['sotano']
      propiedad.terrasa=info['terrasa']
      propiedad.descripcion=info['descripcion']
      propiedad.precio=info['precio']
      
      
      propiedad.save()
      return('inicio')
    else:
      messages.info(request,'Algo salio mal')
            #return redirect ('inicio')
          
          
  form= datos_propiedad_form(initial={'dueño':propiedad.dueño,
                                      'tipo': propiedad.tipo,
                                      'estado': propiedad.estado,
                                      'pais': propiedad.pais,
                                      'provincia' :propiedad.provincia,
                                      'localidado': propiedad.localidado,
                                      'parcela': propiedad.parcela,
                                      'lote': propiedad.lote,
                                      'tamaño' : propiedad.tamaño,
                                      'metros2' : propiedad.metros2,
                                      'clave' : propiedad.clave, 
                                      
                                      
                                      'titular':propiedad.titular,
                                      'propiedad' : propiedad.propiedad,
                                      'ambientes': propiedad.ambientes,
                                      'baños': propiedad.baños,
                                      'dormitorios' : propiedad.dormitorios,
                                      'cocina' : propiedad.cocina,
                                      'living' : propiedad.living,
                                      'garage' : propiedad.garage,
                                      'sotano' : propiedad.sotano,
                                      'terrasa' : propiedad.terrasa,
                                      'descripcion' : propiedad.descripcion,
                                      'precio'  : propiedad.precio,
                                      
                                      })
      
  



def delete(request,id):
  propiedades = datos_propiedad_model.objects.filter(id=id)
  if len(propiedades)!=0:
    propiedad = propiedades[0]
    propiedad.delete()
    
    return render (request,'bd_app/inicio.html')