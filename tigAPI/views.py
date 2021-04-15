from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from tigAPI.models import Product
from tigAPI.serializers import ProductSerializer
from django.http import Http404, JsonResponse

# Products Details #

class ProductsDetailsList(APIView):
    def get(self, request, format=None):
        products = []
        for product in Product.objects.all():
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)

class ProductDetails(APIView):
    def get_object(self, tigID):
        try:
            return Product.objects.get(tigID=tigID)
        except:
            raise Http404

    def get(self, request, tigID, format=None):
        product = self.get_object(tigID)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

####################


# Create your views here.
