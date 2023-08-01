from rest_framework import serializers
from .models import Conocimiento,Tema,Seccion

class ConocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conocimiento
        #fields = ('pregunta','respuesta','tema')
        fields = '__all__'
        
        
class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'
        
        
class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'