from rest_framework import viewsets
from erp_system.serializers.manager1 import productSerializer
from erp_system.models.manager1 import product
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer

    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        brand = request.query_params.get('brand', None)
        if brand:
            self.queryset = self.queryset.filter(brand=brand)
        return super().list(request, *args, **kwargs)


