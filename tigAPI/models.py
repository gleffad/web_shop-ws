from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    quantity_saled = models.IntegerField(default=0)
    commentary = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.