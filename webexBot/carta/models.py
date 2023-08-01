from django.db import models

# Create your models here.
    
    
class TemaCarta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class SeccionCarta(models.Model):
    nombre = models.CharField(max_length=50)
    tema = models.ForeignKey(TemaCarta,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    
class Carta(models.Model):
    pregunta = models.CharField('Nombre del conocimiento', max_length=50)
    respuesta = models.TextField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True,verbose_name="Modificado")
    seccion = models.ForeignKey(SeccionCarta,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.pregunta
    
    
  
        
        


    
    