from django.contrib import admin
from .models import Conocimiento,Seccion,Tema

# Register your models here.

@admin.register(Conocimiento)
class ConocomientoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ('pregunta','tema','seccion','created','modified')
    list_filter = ('tema','seccion')
   


admin.site.register(Tema)
admin.site.register(Seccion)