from rest_framework import viewsets
from erp_system.serializers.manager1 import productSerializer
from erp_system.models.manager1 import product
from rest_framework.pagination import PageNumberPagination
from erp_system.all_permissions import Manager1Permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters import rest_framework as django_filters
from erp_system.filters import Manager1Filter

class CustomPagination(PageNumberPagination):
    page_size = 10


class productViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [Manager1Permissions]
    queryset = product.objects.all()
    serializer_class = productSerializer

    pagination_class = CustomPagination
    filter_backends = (filter.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = Manager1Filter
    search_fields = ('name', 'description')

    def list(self, request, *args, **kwargs):
        brand = request.query_params.get('brand', None)
        if brand:
            self.queryset = self.queryset.filter(brand=brand)
        return super().list(request, *args, **kwargs)


