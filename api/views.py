import json

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response as response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated 
from rest_framework import filters

from core.models import Funcionarios, Empresas
from api.serializers import EmpresasSerializer, FuncionariosSerializer

# Create your views here.

class EmpresasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #simple security method
    '''
    Actions performed without filtering a specific object
    '''
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    lookup_field = 'razao_social'

    '''
    Actions performed filtering a specific object
    '''

class FuncionariosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #simple security method
    '''
    Actions performed without filtering a specific object
    '''

    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer
    lookup_field = 'username'
    