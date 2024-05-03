from django.db import models
from .manager2 import warehouse_product


class customer(models.Model):
    CASH = 'cash'
    ONLINE_PAYMENT = 'online_payment'

    PAY_METHODS = (
        (CASH, 'cash'),
        (ONLINE_PAYMENT, 'online_payment'),
    )

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    product = models.ForeignKey(warehouse_product, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    cash = models.CharField(max_length=200, choices=PAY_METHODS, default=CASH)

    def __str__(self):
        return f"{self.name} {self.phone_number}"
