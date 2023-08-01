from django import forms
from django.contrib import admin
from .models import TemaCarta, SeccionCarta, Carta

class CartaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'seccion_with_tema')
    list_filter = ('seccion__tema', 'seccion')
    
    def seccion_with_tema(self, obj):
        return f"{obj.seccion.nombre} - {obj.seccion.tema.nombre}"
    
    seccion_with_tema.short_description = 'Seccion con Tema'



admin.site.register(TemaCarta)
admin.site.register(SeccionCarta)
admin.site.register(Carta,CartaAdmin)

