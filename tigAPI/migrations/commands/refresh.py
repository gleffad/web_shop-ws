from django.core.management.base import BaseCommand, CommandError
from tigAPI.models import Product
from tigAPI.serializers import ProductSerializer

class Command(BaseCommand):