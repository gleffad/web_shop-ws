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
                    'tigID': int(product['id']),
                    'name': str(product['name']), 
                    'price': float(product['price']),
                    'sale': bool(product['sale']),
                    'sale_price': (product['price'] - ((product['discount'] * product['price']) / 100)) if product['sale'] else 0,
                    'discount': int(product['discount']),
                    'quantity': int(0),
                    'quantity_saled': int(0),
                    'comment': product['comments']
                })

                # print(product['name'])
                
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
                else :
                    print(serializer.errors)