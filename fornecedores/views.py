from rest_framework import viewsets
from fornecedores.models import fornecedores
from fornecedores.serializer import fornecedoresSerializer

class fornecedoresViewSet(viewsets.ModelViewSet):
    queryset = fornecedores.objects.all()
    serializer_class = fornecedoresSerializer