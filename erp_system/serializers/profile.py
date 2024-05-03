from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "role", "is_active", "is_staff", "created_at"]
        read_only_fields = ["id"]

