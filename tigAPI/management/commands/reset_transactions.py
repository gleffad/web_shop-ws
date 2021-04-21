from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Transaction as MTransaction
from tigAPI.serializers import TransactionSerializer
import json
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        # transaction reset
        file = open('tigAPI/ressources/transactions.json')
        #log = open('tigAPI/activity_log.txt')
        self.stdout.write('['+time.ctime()+'] Resetting transactions...')
        #log.write('['+time.ctime()+'] Resetting transactions...')
        jsondata = json.load(file)
        MTransaction.objects.all().delete()
        for transaction in jsondata:
            serializer = TransactionSerializer(data={
                'date': str(transaction['date']),
                'price': float(transaction['price']),
                'quantity': int(transaction['quantity']),
                'tigID': int(transaction['tigID']),
                'operation': int(transaction['operation'])
            })
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    '['+time.ctime()+'] Successfully added transaction from "%s"' % transaction['date']))
        self.stdout.write('['+time.ctime()+'] MTransaction reset terminated.')
        #log.write('['+time.ctime()+'] MTransaction reset terminated.')
        file.close()
        #log.close()
