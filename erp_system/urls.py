from erp_system.views.manager1 import productViewSet
from rest_framework import routers
from django.urls import path, include
from erp_system.views.manager2 import brandViewSet, warehouse_productViewSet
from erp_system.views.manager3 import filialViewSet, filial_productViewSet
from .replenish_stock import admin_replenish_stock
from erp_system.views.cashier import customerViewSet, story_productViewSet
from erp_system.views.profile import ProfileUserView

router = routers.DefaultRouter()
router.register(r'manager1/products', productViewSet)
router.register(r'manager2/brand', brandViewSet)
router.register(r'manager2/warehouse_products', warehouse_productViewSet)
router.register(r'manager3/filial', filialViewSet)
router.register(r'manager3/filial_products', filial_productViewSet)
router.register(r'cashier/customer', customerViewSet)
router.register(r'cashier/story_products', story_productViewSet, basename='story_product')

urlpatterns = [
    path('', include(router.urls)),
    path('replenish_stock/<int:warehouse_product_id>/<int:count>', admin_replenish_stock, name='admin_replenish_stock'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]

