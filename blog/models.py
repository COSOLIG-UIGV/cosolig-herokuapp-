from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    evento_activo =models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=200)
    banner =models.ImageField(upload_to='static/upload/', verbose_name='Banner')
    banner_grande =models.ImageField(upload_to='static/upload/', verbose_name='Flyer')
    contenido = models.TextField(max_length=200)
    fecha_evento = models.DateTimeField(default=timezone.now())
    lugar =models.CharField(max_length=100)
    registro = models.URLField()
    capacidad = models.IntegerField(max_length=4)
    tema = models.CharField(max_length=10)
    expositor = models.CharField(max_length=50)
    usuario = models.ForeignKey(User)


    def __unicode__(self):
        return self.titulo
# Create your models here.
#class Registro()
class Miembros(models.Model):

     miembro_activo = models.BooleanField(default=True)
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=60)
     perfil=models.ImageField(upload_to='static/upload/',verbose_name='Foto de perfil')
     perfil_json=models.URLField(max_length=200,blank=True, null= False)
     correo =models.EmailField(max_length=70,blank=True, null= True, unique= True)
     COMUNIDAD_UIGV = (
        ('CS','COSOLIG'),
        ('CH','CHIAS-GRUPO ROBOTICA'),
        )
     tipo =models.CharField(max_length=6,choices=COMUNIDAD_UIGV)

     TYPE_CHOICES = (
       ('PR', 'Presidente'),
       ('VP', 'Vice-Presidente'),
       ('2VP', '2da Vice-Presidente'),
       ('SE','Secretario'),
       ('TS','Tesorero') ,
     )
     cargo =models.CharField(max_length=6,choices=TYPE_CHOICES)
     def __unicode__(self):
         return self.cargo
