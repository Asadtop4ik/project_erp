from django.db import models


class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    first_price = models.FloatField(max_length=200)
    sale_price = models.FloatField(max_length=200)
    brand = models.CharField(max_length=200)
    reg_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    where_to = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

