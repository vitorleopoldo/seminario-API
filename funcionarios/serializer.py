from rest_framework import serializers
from funcionarios.models import funcionarios

class funcionariosSerializer(serializers.ModelSerializer):
    class Meta:

        model = funcionarios
        fields = '__all__'