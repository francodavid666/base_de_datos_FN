from django.db import models

# Create your models here.


 
    
    
class datos_propiedad_model(models.Model):
    CASA='Casa'
    DEPARTAMENTO= 'Departamento'
    TERRENO= 'Terreno'
    LOCAL_COMERCIAL='Local comercial'
    PH = 'PH'
    QUINTA_VACACIONAL='Quinta vacacacional'
    OFICINA_COMERCIAL= 'Oficina comercial'
    GARAGE= 'Garage'
    BODEGA_GALPON= 'Bodega-Galpon'
    FCOMERCIO= 'Fondo de comercio'
    HOTEL= 'Hotel'
    DEPOSITO= 'Deposito'
    BODEGA= 'Bodega, niho o parcela'
    CONSULTORIO= 'Consultorio'
    
    OPCIONES=[(CASA,'Casa'),
              (DEPARTAMENTO, 'Departamento'),
              (TERRENO,'terreno'),
              (LOCAL_COMERCIAL,'Local comercial'),
              (PH,'ph'),
              (QUINTA_VACACIONAL,'Quinta vacacional'),
              (OFICINA_COMERCIAL,'Oficina comercial'),
              (GARAGE, 'Garage'),
              (BODEGA_GALPON, 'Bodega-Galpon'),
              (FCOMERCIO, 'Fondo de comercio'),
              (HOTEL, 'Hotel'),
              (DEPOSITO, 'Deposito'),
              (BODEGA, 'Bodega, niho o parcela'),
              (CONSULTORIO, 'Consultorio'),
              ]
    
    
    DIS='Disponible'
    ALQ='Alquilado'
    ENAL= 'En alquiler'
    ENV= 'En venta'
    POR = 'Por vender'
    VN= 'Vendido'
    
    OPCIONES_ESTADO=[(DIS,'Disponible'),
                     (ENAL,'En alquiler'),
                     (ALQ,'Alquilado'),
                     (ENV,'En venta'),
                     (POR,'Por vender'),
                     (VN,'Vendido')]
    id = models.AutoField(primary_key=True)
    dueño= models.CharField(max_length=50,blank=True)                   
    tipo = models.CharField(choices=OPCIONES,
                            max_length=50,
                            default=CASA,
                            null=True,
                            blank = True) 
    
    
    estado = models.CharField(max_length=50,null=True,blank=False,
                              choices=OPCIONES_ESTADO,
                              default=DIS,)
    direccion = models.CharField(max_length=50,null=True,blank=False)
    descripcion= models.CharField(max_length=200,null=True,blank=False)
    pais= models.CharField(max_length=50,blank = True,null=True)
    provincia = models.CharField(max_length=50,blank = True,null=True)
    localidad = models.CharField(max_length=50,blank = True,null=True)
    parcela= models.IntegerField(null=True,blank=False)
    lote= models.CharField(max_length=50,null=True,blank=False)
    tamaño= models.CharField(max_length=50,null=True,blank=False)
    metros2 = models.CharField(max_length=50,null=True,blank=False)
    clave_c=models.CharField(max_length=50,null=True,blank=False)
    
    titular = models.CharField(max_length=50,null=True,blank=False)
    
    
    MN='Monoambiente'
    DOS='2 Ambientes'
    TRES='3 Ambientes'
    CUATRO='4 Ambientes'
    CINCO='5 Ambientes'
    
    OPCIONES_AMBIENTES=[(MN,'Monoambiente'),
                        (DOS,'2 Ambientes'),
                        (TRES,'3 Ambientes'),
                        (CUATRO,'4 Ambientes'),
                        (CINCO,'5 Ambientes')]
    
    
    propiedad = models.CharField(max_length=200,null=True,blank=False)
    
    
    ambientes= models.CharField(max_length=50,null=True,blank=False,
                             choices=OPCIONES_AMBIENTES,
                             default= MN)
    baños= models.IntegerField(null=True,blank=False)
    dormitorios= models.IntegerField(null=True,blank=False)
    cocina= models.IntegerField(null=True,blank=False)
    living= models.IntegerField(null=True,blank=False)
    comedor= models.IntegerField(null=True,blank=False)
    garage= models.IntegerField(null=True,blank=False)
    sotano=models.IntegerField(null=True,blank=False)
    terrasa= models.IntegerField(null=True,blank=False)
    
    descripcion= models.CharField(max_length=200,null=True,blank=False)
    precio= models.CharField(max_length=20,null=True,blank=False)
    
      
    def __str__(self)-> str:
         return self.propiedad+' '+ self.direccion
   
    

