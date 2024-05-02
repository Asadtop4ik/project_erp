from rest_framework import viewsets, response
from erp_system.serializers.manager3 import filialSerializer, filial_productSerializer
from erp_system.models.manager3 import filial, filial_product
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from erp_system.all_permissions import Manager3Permissions


class filialViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager3Permissions]
    queryset = filial.objects.all()
    serializer_class = filialSerializer

    @action(detail=True, methods=['get'])
    def filial_products(self, requests, pk=None):
        filial = self.get_object()
        filial_products = filial.filial_product_set.all()
        serializer = filial_productSerializer(filial_products, many=True)
        return response.Response(serializer.data)


class CustomPagination(PageNumberPagination):
    page_size = 10


class filial_productViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager3Permissions]
    queryset = filial_product.objects.all()
    serializer_class = filial_productSerializer

    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        filial_id = request.query_params.get('filial_id', None)
        if filial_id:
            self.queryset = self.queryset.filter(filial=filial_id)
        return super().list(request, *args, **kwargs)
