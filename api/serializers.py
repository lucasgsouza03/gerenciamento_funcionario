from rest_framework import serializers
from core.models import Funcionarios, Empresas

'''
Serialization based on Model Funcionarios
'''
class FuncionariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Funcionarios
        fields = ('first_name', 'last_name', 'email', 'cargo', 'idade', 'username', 'password', 'empresa')
        extra_kwargs = {'password': {'write_only':True}, 'empresas': {'required': False}}
    
    def create(self, validated_data):
        """ Creates and returns a new user """

        # Validating Data
        user = Funcionarios(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        email=validated_data['email'],
        cargo=validated_data['cargo'],
        idade=validated_data['idade'],
        username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

'''
Serialization based on Model Empresas
'''
class EmpresasSerializer(serializers.ModelSerializer):
    funcionarios = FuncionariosSerializer(many=True, read_only=True)
    class Meta:
        model = Empresas
        fields = ('nome_fantasia', 'localizacao', 'razao_social', 'cnpj', 'funcionarios')
        extra_kwargs = {'funcionarios': {'required': False}}
