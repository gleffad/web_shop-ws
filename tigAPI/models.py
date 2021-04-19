from django.db import models

class Product(models.Model):
    TigID = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    sale = models.BooleanField(default=False)
    sale_price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    qte_stock = models.IntegerField(default=0)
    qte_sold = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(default=-1)
    class Meta:
        ordering = ('TigID')

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    TigID = models.IntegerField()
    category = models.IntegerField(max_length=255)
    class Meta:
        ordering = ('created')