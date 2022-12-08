from rest_framework import serializers
from notafiscal.models import notafiscal

class notafiscalSerializer(serializers.ModelSerializer):
    class Meta:

        model = notafiscal
        fields = '__all__'