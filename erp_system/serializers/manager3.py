from rest_framework import serializers
from erp_system.models.manager3 import filial, filial_product
from erp_system.models.manager2 import warehouse_product

class filialSerializer(serializers.ModelSerializer):
    class Meta:
        model = filial
        fields = '__all__'


class filial_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = filial_product
        fields = '__all__'

        def validate_quantity(self, value):
            try:
                product_id = self.initial_data['product']
                product = warehouse_product.objects.get(id=product_id)

                if value > product.stock:
                    raise serializers.ValidationError("Not enough stock")

                if value < 1:
                    raise serializers.ValidationError("Quantity must be greater than 1")

                return value

            except warehouse_product.DoesNotExist:
                raise serializers.ValidationError("Product does not exist")

        def create(self, validated_data):
            count = filial_product.objects.create(**validated_data)
            product = count.product
            product.stock -= count.quantity
            product.save()
            return count
