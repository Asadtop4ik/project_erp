from rest_framework import serializers
from django.contrib.auth import get_user_model
from erp_system.models.manager1 import product
User = get_user_model()


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
