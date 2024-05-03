from rest_framework import viewsets, filters
from erp_system.models.cashier import customer
from erp_system.serializers.cashier import customerSerializer, story_productSerializer
from .manager2 import CustomPagination
from erp_system.models.manager2 import warehouse_product
from django_filters import rest_framework as django_filters
from erp_system.filters import Manager2Filter
from rest_framework.parsers import MultiPartParser, FormParser
from erp_system.all_permissions import CashierPermissions


class customerViewSet(viewsets.ModelViewSet):
    permission_classes = [CashierPermissions]
    queryset = customer.objects.all()
    serializer_class = customerSerializer


class story_productViewSet(viewsets.ModelViewSet):
    permission_classes = [CashierPermissions]
    parser_classes = (MultiPartParser, FormParser,)
    queryset = warehouse_product.objects.all()
    serializer_class = story_productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = Manager2Filter
    search_fields = ['name', 'description', 'brand']
