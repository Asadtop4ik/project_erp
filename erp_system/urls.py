from erp_system.views.manager1 import productViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products', productViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

