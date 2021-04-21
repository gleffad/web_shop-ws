from django.db import models


class Product(models.Model):
    tigID = models.IntegerField()
    name = models.CharField(max_length=255)
    on_sale = models.BooleanField(default=False)
    producer_price = models.FloatField(default=0)
    retail_price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    qty_stock = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    category = models.IntegerField(default=-1)

    class Meta:
        ordering = ('tigID',)


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    tigID = models.IntegerField()
    operation = models.IntegerField(default=-1)

    class Meta:
        ordering = ('date',)


class User(models.Model):
    account_creation_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)