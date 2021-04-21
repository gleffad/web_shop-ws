from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Transaction as MTransaction
from tigAPI.serializers import TransactionSerializer
import json
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        # transaction reset
        file = open('tigAPI/ressources/transactions.json')
        #log = open('tigAPI/activity_log.txt')
        self.stdout.write('['+str(datetime.now())+'] Resetting transactions...')
        #log.write('['+str(datetime.now())+'] Resetting transactions...')
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
                    '['+str(datetime.now())+'] Successfully added transaction from "%s"' % transaction['date']))
        self.stdout.write('['+str(datetime.now())+'] MTransaction reset terminated.')
        #log.write('['+str(datetime.now())+'] MTransaction reset terminated.')
        file.close()
        # log.close()
