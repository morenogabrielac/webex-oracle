from rest_framework import serializers
from .models import Carta,TemaCarta,SeccionCarta


class TemaCartaSerializer(serializers.ModelSerializer):
    class Meta:
        model=TemaCarta
        #fields = ('pregunta','respuesta','tema')
        fields = '__all__'
        
class SeccionCartaSerializer(serializers.ModelSerializer):
    #tema = serializers.StringRelatedField()
    nombre_tema = serializers.CharField(source='tema.nombre',read_only=True)
    class Meta:
        model=SeccionCarta
        #fields = ('pregunta','respuesta','tema')
        fields = '__all__'

class CartaSerializer(serializers.ModelSerializer):
    seccion = SeccionCartaSerializer()
    
    class Meta:
        model=Carta
        #fields = ('pregunta','respuesta','tema')
        fields = '__all__'
        