from rest_framework import serializers
from erp_system.models.manager1 import product


class productSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = product
        fields = '__all__'
