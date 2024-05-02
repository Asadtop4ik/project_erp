from django.db import models
from .manager2 import brand


class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    first_price = models.FloatField(max_length=200)
    sale_price = models.FloatField(max_length=200)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    reg_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    where_to = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

