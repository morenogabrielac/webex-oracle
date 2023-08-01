from django.db import models

# Create your models here.
class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    
class Tema(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



        

class Conocimiento(models.Model):
    pregunta = models.CharField('Nombre del conocimiento', max_length=50)
    respuesta = models.TextField()
    seccion = models.ForeignKey(Seccion,on_delete=models.PROTECT)
    tema = models.ForeignKey(Tema,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True,verbose_name="Modificado")
    
    def __str__(self):
        return self.pregunta
    
    