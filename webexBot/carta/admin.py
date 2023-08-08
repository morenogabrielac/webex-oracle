from django import forms
from django.contrib import admin
from .models import TemaCarta, SeccionCarta, Carta


class CartaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'seccion_with_tema')
    list_filter = ('seccion__tema', 'seccion')
    
    def seccion_with_tema(self, obj):
        return f"{obj.seccion.nombre} - {obj.seccion.tema.nombre}"
    
    seccion_with_tema.short_description = 'Seccion - Tema'
    
    

#-----------------------------------------Visualizacion mas limpia que el de arriba---------------------------------------------------------------
class SeccionCartaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tema_nombre')

    def tema_nombre(self, obj):
        return obj.tema.nombre
    
    tema_nombre.short_description = 'Tema'

class CartaAdmin_v3(admin.ModelAdmin):
    list_display = ('pregunta', 'seccion_nombre', 'seccion_tema')
    list_filter = ('seccion__tema', 'seccion')
    search_fields = ('pregunta', 'respuesta', 'seccion__nombre', 'seccion__tema__nombre')
   

    def seccion_nombre(self, obj):
        return obj.seccion.nombre
    
    def seccion_tema(self, obj):
        return obj.seccion.tema.nombre
    
    seccion_nombre.short_description = 'Sección'
    seccion_tema.short_description = 'Tema de la Sección'
    
#-----------------------------------------Testeando---------------------------------------------------------------    
    

    
    

admin.site.register(TemaCarta)
admin.site.register(SeccionCarta,SeccionCartaAdmin)
admin.site.register(Carta,CartaAdmin_v3)

