from django.urls import path,include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(prefix=r'conocimientos',viewset=views.ConocimientoViewSet)
router.register(prefix=r'temas',viewset=views.TemaViewSet)
router.register(prefix=r'secciones',viewset=views.SeccionViewSet)

urlpatterns = [
    path('', include(router.urls))
]