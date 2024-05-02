from django_filters import rest_framework as django_filters
from erp_system.models.manager1 import product
from erp_system.models.manager2 import warehouse_product
from erp_system.models.manager3 import filial_product


class Manager1Filter(django_filters.FilterSet):
    class Meta:
        model = product
        fields = ['brand']


class Manager2Filter(django_filters.FilterSet):
    class Meta:
        model = warehouse_product
        fields = ['brand']


class Manager3Filter(django_filters.FilterSet):
    class Meta:
        model = filial_product
        fields = ['filial']