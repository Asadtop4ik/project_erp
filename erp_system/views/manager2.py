from django_filters import rest_framework as django_filters
from rest_framework import viewsets, filters
from erp_system.serializers.manager2 import brandSerializer, warehouse_productSerializer
from erp_system.models.manager2 import brand, warehouse_product
from erp_system.all_permissions import Manager2Permissions
from rest_framework.parsers import MultiPartParser, FormParser
from erp_system.filters import Manager2Filter
from .manager1 import CustomPagination


class brandViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager2Permissions]
    queryset = brand.objects.all()
    serializer_class = brandSerializer


class warehouse_productViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [Manager2Permissions]
    queryset = warehouse_product.objects.all()
    serializer_class = warehouse_productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = Manager2Filter
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        warehouse_brand = request.query_params.get('brand', None)
        if warehouse_brand:
            self.queryset = self.queryset.filter(brand=warehouse_brand)
        return super().list(request, *args, **kwargs)

