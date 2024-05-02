from rest_framework import serializers
from erp_system.models.manager1 import product


class productSerializer(serializers.ModelSerializer):
    background_img = serializers.ImageField()

    class Meta:
        model = product
        fields = '__all__'

