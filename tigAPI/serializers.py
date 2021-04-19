from rest_framework.serializers import ModelSerializer
from tigAPI.models import Product, Transaction

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('TigID', 'name', 'price', 'sale', 'sale_price',
                  'discount', 'quantity', 'quantity_saled', 'comment')

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('created', 'price', 'quantity', 'TigID', 'type')