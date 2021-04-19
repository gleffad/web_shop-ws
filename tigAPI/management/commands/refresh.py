from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Product, Transaction
from tigAPI.serializers import ProductSerializer, TransactionSerializer
from tigAPI.config import baseUrl
import requests
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        # product refresh
        self.stdout.write('['+time.ctime()+'] Refreshing list of products...')
        ids = Product.objects.values_list('TigID', flat=True)
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for product in jsondata:
            if product['TigID'] not in ids:
                serializer = ProductSerializer(data={
                    'TigID': int(product['TigID']),
                    'name': str(product['name']),
                    'price': float(product['price']),
                    'sale': bool(product['sale']),
                    'sale_price': (product['price'] - ((product['discount'] * product['price']) / 100)) if product['sale'] else 0,
                    'discount': int(product['discount']),
                    'qte_stock': int(0),
                    'qte_sold': int(0),
                    'comment': str(product['comments']),
                    'category': int(product['category'])
                })
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS(
                        '['+time.ctime()+'] Successfully added product TigID="%s"' % product['TigID']))
                else:
                    self.stderr(self.style.ERROR(serializer.errors))
        self.stdout.write('[' + time.ctime() + '] Refresh ran successfully')
        # Transaction refresh
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'transactions/')
        jsondata = response.json()
        Transaction.objects.all().delete()
        for transaction in jsondata:
            serializer = TransactionSerializer(data={
                'price': str(transaction['price']),
                'availability': str(transaction['availability']),
                'price': str(transaction['sale']),
                'TigID': int(transaction['TigID']),
                'category': str(transaction['name'])
            })
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    '['+time.ctime()+'] Successfully added productsQuantity TigID="%s"' % product['TigID']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')