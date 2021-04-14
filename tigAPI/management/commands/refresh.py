from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Product
from tigAPI.serializers import ProductSerializer
from tigAPI.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh Products list'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing list of products...')
        ids = Product.objects.values_list('tigID', flat=True)
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for product in jsondata:
            if product['id'] not in ids:
                serializer = ProductSerializer(data={ 
                    'tigID': str(product['id']),
                    'name': str(product['name']), 
                    'price': str(product['price']),
                    'sale': str(product['sale']),
                    'sale_price': str(product['discount'] * product['price']) if product['sale'] else str(product['sale']),
                    'discount': str(product['discount']),
                    'quantity': str(0),
                    'quantity_saled': str(0),
                    'comment': str(product['comments'])
                })
                
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))