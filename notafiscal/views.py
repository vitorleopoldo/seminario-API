from rest_framework import viewsets
from notafiscal.models import notafiscal
from notafiscal.serializer import notafiscalSerializer

class notafiscalViewSet(viewsets.ModelViewSet):
    queryset = notafiscal.objects.all()
    serializer_class = notafiscalSerializer