from rest_framework.serializers import ModelSerializer
from tigAPI.models import Product as MProduct
from tigAPI.models import Transaction as MTransaction
from tigAPI.models import User as MUser


class ProductSerializer(ModelSerializer):
    class Meta:
        model = MProduct
        fields = ('tigID', 'name', 'on_sale', 'producer_price', 'retail_price', 'discount_price',
                  'discount', 'qty_stock', 'qty_sold', 'comment', 'category')


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = MTransaction
        fields = ('date', 'price', 'quantity', 'tigID', 'operation')


class UserSerializer(ModelSerializer):
    class Meta:
        model = MUser
        fields = ('account_creation_date', 'user_name', 'password')
