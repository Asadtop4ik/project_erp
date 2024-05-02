from rest_framework import serializers
from erp_system.models.manager2 import brand, warehouse_product


class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = '__all__'


class warehouse_productSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = warehouse_product
        fields = '__all__'
