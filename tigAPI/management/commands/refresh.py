from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Product as MProduct
from tigAPI.serializers import ProductSerializer
from tigAPI.config import baseUrl
import requests
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        # product refresh
        self.stdout.write('['+datetime.now()+'] Refreshing list of products...')
        ids = MProduct.objects.values_list('tigID', flat=True)
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for product in jsondata:
            if product['id'] not in ids:
                serializer = ProductSerializer(data={
                    'tigID': int(product['id']),
                    'name': str(product['name']),
                    'on_sale': bool(product['sale']),
                    'producer_price': float(product['price'] - ((product['discount'] * product['price']) / 100) if product['sale'] else product['price']),
                    'retail_price': float(2 * product['price']),
                    'discount_price': float(0),
                    'discount': int(0),
                    'qty_stock': int(0),
                    'qty_sold': int(0),
                    'comments': str(product['comments']),
                    'category': int(product['category'])
                })
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS(
                        '['+datetime.now()+'] Successfully added product tigID="%s"' % product['id']))
                else:
                    self.stderr(self.style.ERROR(serializer.errors))
        self.stdout.write('[' + datetime.now() + '] Refresh ran successfully')
