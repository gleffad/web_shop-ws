from rest_framework.serializers import ModelSerializer
from mytig.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'sale_price', 'discount', 'quantity', 'quantity_saled', 'commentary')