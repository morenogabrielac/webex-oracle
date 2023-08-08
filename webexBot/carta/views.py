
from django.shortcuts import render
from rest_framework import viewsets,generics, status
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializer import CartaSerializer,TemaCartaSerializer,SeccionCartaSerializer
from .models import Carta,TemaCarta,SeccionCarta


from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CartaViewSet(viewsets.ModelViewSet):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer
    
class TemaCartaViewSet(viewsets.ModelViewSet):
    queryset = TemaCarta.objects.all()
    serializer_class = TemaCartaSerializer
    
class SeccionCartaViewSet(viewsets.ModelViewSet):
    queryset = SeccionCarta.objects.all()
    serializer_class = SeccionCartaSerializer
    
    
class CartaConSeccion(APIView):
    def get (self,request,*args,**kwargs):
        cartas = Carta.objects.select_related('seccion').all()
        data = []
        for carta in cartas:
            data.append({
                
                'pregunta':carta.pregunta,
                'respuesta':carta.respuesta,
                'created':carta.created,
                'modified':carta.modified,
                'seccion':carta.seccion.nombre
                    
            })
            
        return Response(data)

class CartaPorTemaAPIView(generics.ListAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','seccion__tema']
    
class SeccionPorTemaAPIView(generics.ListAPIView):
    queryset = SeccionCarta.objects.all()
    serializer_class = SeccionCartaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','tema']