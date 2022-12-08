from rest_framework import viewsets
from vendas.models import vendas
from vendas.serializer import vendasSerializer

class vendasViewSet(viewsets.ModelViewSet):
    queryset = vendas.objects.all()
    serializer_class = vendasSerializer