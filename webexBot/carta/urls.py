from django.urls import path,include
from rest_framework import routers
from carta import views

router = routers.DefaultRouter()
router.register(prefix=r'cartas',viewset=views.CartaViewSet)
router.register(prefix=r'temas',viewset=views.TemaCartaViewSet)
router.register(prefix=r'secciones',viewset=views.SeccionCartaViewSet)
#router.register(prefix=r"cartaSeccionada",viewset=views.CartaConSeccion.as_view())

urlpatterns = [
    path('', include(router.urls)), 
    path('cartas/tema/<int:tema_nombre>/', views.CartaPorTemaAPIView.as_view(), name='cartas-por-tema'),
    
    
    
]