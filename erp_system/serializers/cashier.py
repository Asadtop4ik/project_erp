from rest_framework import serializers
from erp_system.models.cashier import customer
from erp_system.models.manager2 import warehouse_product
from django.core.exceptions import ObjectDoesNotExist


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

    def validate_quantity(self, value):
        try:
            product_id = self.initial_data['warehouse_product_id']
            product = warehouse_product.objects.get(id=product_id)

            if value > product.stock:
                raise serializers.ValidationError("Not enough stock")

            elif value < 1:
                raise serializers.ValidationError("Quantity must be greater than 1")

            return value

        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product does not exist")

    def create(self, validated_data):
        count = customer.objects.create(**validated_data)
        archive_product = count.product
        archive_product.stock -= count.amount
        archive_product.save()
        return count


class story_productSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = warehouse_product
        fields = ["name", "stock", "first_price", "image", "brand"]

