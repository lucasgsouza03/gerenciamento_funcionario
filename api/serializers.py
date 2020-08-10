from rest_framework import serializers
from core.models import Funcionarios, Empresas

'''
Serialization based on Model Empresas
'''
class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
        extra_kwargs = {'funcionario': {'required': False}}

'''
Serialization based on Model Funcionarios
'''
class FuncionariosSerializer(serializers.ModelSerializer):
    empresas = EmpresasSerializer(many=True, read_only=True)
    class Meta:
        model = Funcionarios
        fields = ('nome', 'cargo', 'idade', 'username', 'password', 'empresas')
        extra_kwargs = {'password': {'write_only':True}, 'empresas': {'required': False}}
    
    def create(self, validated_data):
        """ Creates and returns a new user """

        # Validating Data
        user = Funcionarios(
        nome=validated_data['nome'],
        cargo=validated_data['cargo'],
        idade=validated_data['idade'],
        username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user