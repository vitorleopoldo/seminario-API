from rest_framework import serializers
from vendas.models import vendas

class vendasSerializer(serializers.ModelSerializer):
    class Meta:

        model = vendas
        fields = '__all__'