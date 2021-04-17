from django.db import models


class Product(models.Model):
    tigID = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    sale = models.BooleanField(default=False)
    sale_price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    quantityInSock = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    tigID = models.IntegerField()
    type = models.CharField(max_length=255)
# Create your models here.
