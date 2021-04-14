from rest_framework.serializers import ModelSerializer
from tigAPI.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('tigID', 'name', 'price', 'sale', 'sale_price', 'discount', 'quantity', 'quantity_saled', 'comment')