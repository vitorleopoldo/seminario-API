from rest_framework import serializers
from produtos.models import produtos

class produtosSerializer(serializers.ModelSerializer):
    class Meta:

        model = produtos
        fields = '__all__'