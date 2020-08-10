from django.test import TestCase

# Create your tests here.
import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from core.models import Empresas, Funcionarios

class AuthTesteCase(APITestCase):

    def test_authentication(self):
        self.user = User.objects.create_user(username='admin', password='admin@123')
        bad_response = self.client.get('/empresa/')
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username='admin', password='admin@123')
        response = self.client.get('/empresa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

class EmpresaViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin@123')
        self.client.login(username='admin', password='admin@123')
        data_func1 = {
            'first_name': 'funcionario',
            'last_name': '1',
            'email': 'funcionario1@email.com',
            'cargo': 'cargo1',
            'idade': 20,
            'username': 'func1',
            'password': 'passfunc1'
        }
        self.client.post('/funcionario/', data=data_func1)
        data_func2 = {
            'first_name': 'funcionario',
            'last_name': '2',
            'email': 'funcionario2@email.com',
            'cargo': 'cargo2',
            'idade': 23,
            'username': 'func2',
            'password': 'passfunc2'
        }
        self.client.post('/funcionario/', data=data_func2)

        data_empresa1 = {
            'nome_fantasia': 'Empesa1', #intentional typing error for update test case
            'localizacao': 'localizacao',
            'razao_social': 'emp1',
            'cnpj': '00.000.000/0001-01',
        }
        response_1 = self.client.post('/empresa/', data=data_empresa1)

    def test_create(self):
        data_empresa2 = {
            'nome_fantasia': 'Empresa2',
            'localizacao': 'localizacao',
            'razao_social': 'emp2',
            'cnpj': '00.000.000/0002-02',
        }
        response_2 = self.client.post('/empresa/', data=data_empresa2)
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
    
    def test_update(self):
        data = {'name': 'Empresa1'}
        response = self.client.patch('/empresa/emp1/', data=data)
        bad_response = self.client.patch('/empresa/bad_pk/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_list(self):
        response = self.client.get('/empresa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter(self):
        response = self.client.get('/empresa/emp1/')
        bad_response = self.client.get('/empresa/bad_pk/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        response = self.client.delete('/empresa/emp1/')
        response_not_found = self.client.delete('/empresa/bad_pk/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)

class FuncionarioViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin@123')
        self.client.login(username='admin', password='admin@123')
        data_empresa1 = {
            'nome_fantasia': 'Empesa1',
            'localizacao': 'localizacao',
            'razao_social': 'emp1',
            'cnpj': '00.000.000/0001-01',
        }
        self.client.post('/empresa/', data=data_empresa1)
        data_empresa2 = {
            'nome_fantasia': 'Empresa2',
            'localizacao': 'localizacao',
            'razao_social': 'emp2',
            'cnpj': '00.000.000/0002-02',
        }
        self.client.post('/empresa/', data=data_empresa2)

        empresa = []
        for emp in Empresas.objects.all():
            empresa.append(emp.id)

        data_func1 = {
            'first_name': 'functionario',
            'last_name': '1',
            'email': 'funcionario1@email.com',
            'cargo': 'cargo1',
            'idade': 20,
            'username': 'func1',
            'password': 'passfunc1',
            'empresa': empresa
        }
        self.client.post('/funcionario/', data=data_func1)

    def test_create(self):
        empresa = []
        empresa.append(Empresas.objects.all()[0].id)
        data_func2 = {
            'first_name': 'funcionario',
            'last_name': '2',
            'email': 'funcionario2@email.com',
            'cargo': 'cargo2',
            'idade': 23,
            'username': 'func2',
            'password': 'passfunc2',
            'empresa': empresa
        }
        response_2 = self.client.post('/funcionario/', data=data_func2)

        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
    
    def test_update(self):
        data = {'first_name': 'funcionario'}
        test = self.client.get('/funcionario/')
        response = self.client.patch('/funcionario/func1/', data=data)
        bad_response = self.client.patch('/funcionario/bad_pk/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_list(self):
        response = self.client.get('/funcionario/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter(self):
        response = self.client.get('/funcionario/func1/')
        bad_response = self.client.get('/funcionario/bad_pk/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        response = self.client.delete('/funcionario/func1/')
        response_not_found = self.client.delete('/funcionario/bad_pk/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)