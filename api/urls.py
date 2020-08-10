from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import EmpresasViewSet, FuncionariosViewSet

router = DefaultRouter()
router.register('empresa', EmpresasViewSet, basename='empresa')
router.register('funcionario', FuncionariosViewSet, basename='funcionario')

urlpatterns = [
    #path(r'^api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)