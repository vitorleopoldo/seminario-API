from rest_framework import viewsets
from funcionarios.models import funcionarios
from funcionarios.serializer import funcionariosSerializer

class funcionariosViewSet(viewsets.ModelViewSet):
    queryset = funcionarios.objects.all()
    serializer_class = funcionariosSerializer