from django.db import models


class brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class warehouse_product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    where_to = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    first_price = models.CharField(max_length=200)
    sale_price = models.CharField(max_length=200)
    reg_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def is_in_count(self):
        return self.stock > 0

    def reduce_count(self, quantity):
        if self.stock < quantity:
            return False
        self.stock -= quantity
        self.save()
        return True

    def increase_stock(self, quantity):
        self.stock += quantity
        self.save()

    class Meta:
        ordering = ['name']