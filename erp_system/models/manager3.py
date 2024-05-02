from django.db import models
from .manager2 import warehouse_product


class filial(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class filial_product(models.Model):
    filial = models.ForeignKey(filial, on_delete=models.CASCADE)
    product = models.ForeignKey(warehouse_product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.filial.name

