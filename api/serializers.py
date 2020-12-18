from rest_framework import serializers
from AppTeste.models import *

class EstadoSerializer(serializers.ModelSerializer):
    descricao = serializers.CharField() 
    uf: serializers.CharField()

    class Meta:
        model = Estado
        fields = ['id', 'descricao', 'uf']

        
class MunicipioSerializer(serializers.ModelSerializer):
    descricao = serializers.CharField()

    class Meta:
        model = Municipio
        fields = ['id', 'descricao', 'area', 'estado', 'populacao']
        


class TesteQuerySerializer(serializers.ModelSerializer):
    descricao = serializers.CharField()

    class Meta:
        model = Teste
        fields = ['id', 'descricao', 'nome_estado']