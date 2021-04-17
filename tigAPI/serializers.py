from rest_framework.serializers import ModelSerializer
from tigAPI.models import Product, Transaction


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('tigID', 'name', 'price', 'sale', 'sale_price',
                  'discount', 'quantity', 'quantity_saled', 'comment')


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('created', 'price', 'quantity', 'tigID', 'type')


class ProductInSale(models.MoVdel):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)
