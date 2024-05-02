from rest_framework import viewsets
from erp_system.serializers.manager1 import productSerializer
from erp_system.models.manager1 import product


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer

