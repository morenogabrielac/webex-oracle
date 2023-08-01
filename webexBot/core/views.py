from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ConocimientoSerializer,TemaSerializer,SeccionSerializer
from .models import Conocimiento,Tema,Seccion

# Create your views here.

class ConocimientoViewSet(viewsets.ModelViewSet):
    queryset = Conocimiento.objects.all()
    serializer_class = ConocimientoSerializer
    
class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    
class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
