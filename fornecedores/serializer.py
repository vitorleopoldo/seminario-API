from rest_framework import serializers
from fornecedores.models import fornecedores

class fornecedoresSerializer(serializers.ModelSerializer):
    class Meta:

        model = fornecedores
        fields = '__all__'