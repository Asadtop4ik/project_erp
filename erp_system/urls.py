from erp_system.views.manager1 import productViewSet
from rest_framework import routers
from django.urls import path, include
from erp_system.views.manager2 import brandViewSet, warehouse_productViewSet
from erp_system.views.manager3 import filialViewSet, filial_productViewSet
from .replenish_stock import admin_replenish_stock

router = routers.DefaultRouter()
router.register(r'manager1/products', productViewSet)
router.register(r'manager2/brand', brandViewSet)
router.register(r'manager2/warehouse_products', warehouse_productViewSet)
router.register(r'manager3/filial', filialViewSet)
router.register(r'manager3/filial_products', filial_productViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('replenish_stock/<int:warehouse_product_id>/<int:count>', admin_replenish_stock, name='admin_replenish_stock'),
]

