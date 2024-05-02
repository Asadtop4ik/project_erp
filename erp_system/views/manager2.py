from rest_framework import viewsets
from erp_system.serializers.manager2 import brandSerializer, warehouse_productSerializer
from erp_system.models.manager2 import brand, warehouse_product
from rest_framework.pagination import PageNumberPagination
from erp_system.all_permissions import Manager2Permissions


class brandViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager2Permissions]
    queryset = brand.objects.all()
    serializer_class = brandSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10


class warehouse_productViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager2Permissions]
    queryset = warehouse_product.objects.all()
    serializer_class = warehouse_productSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        warehouse_brand = request.query_params.get('brand', None)
        if warehouse_brand:
            self.queryset = self.queryset.filter(brand=warehouse_brand)
        return super().list(request, *args, **kwargs)

