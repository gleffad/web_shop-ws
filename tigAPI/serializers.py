from rest_framework.serializers import ModelSerializer
from tigAPI.models import Product, Transaction, User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('tigID', 'name', 'on_sale', 'producer_price', 'retail_price', 'discount_price',
                  'discount', 'qty_stock', 'qty_sold', 'comment', 'category')


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('date', 'price', 'quantity', 'tigID', 'operation')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('account_creation_date', 'user_name', 'password')
