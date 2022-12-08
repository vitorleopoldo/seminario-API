from rest_framework import viewsets
from produtos.models import produtos
from produtos.serializer import produtosSerializer

class produtosViewSet(viewsets.ModelViewSet):
    queryset = produtos.objects.all()
    serializer_class = produtosSerializer