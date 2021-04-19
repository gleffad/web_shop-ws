from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from tigAPI.models import Product
from tigAPI.serializers import ProductSerializer
from django.http import Http404, JsonResponse

class ProductsDetailsList(APIView):
    def get(self, request, format=None):
        products = []
        for product in Product.objects.all():
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)

class ProductDetails(APIView):
    def get_object(self, TigID):
        try:
            return Product.objects.get(TigID=TigID)
        except:
            raise Http404
    def get(self, request, TigID, format=None):
        product = self.get_object(TigID)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class DecrementStock(APIView):
    def update_object(self, TigID, number):
        try:
            ProductQuantity.objects.filter(
                TigID=TigID).update(qte_stock=number)
        except ProductQuantity.DoesNotExist:
            raise Http404
    def get(self, request, TigID, number, format=None):
        prod = ProductQuantity.objects.get(TigID=TigID)
        serialize = ProductQuantitySerializer(prod).data
        qte_stock = serialize['qte_stock'] - number
        if qte_stock >= 0:
            self.update_object(TigID, qte_stock)
        else:
            raise Http404
        update(TigID)
        prod = ProductQuantity.objects.get(TigID=TigID)
        serialize = ProductQuantitySerializer(prod).data
        return Response(serialize)

class IncrementStock(APIView):
    def update_object(self, TigID, number):
        try:
            ProductQuantity.objects.filter(
                TigID=TigID).update(qte_stock=number)
        except ProductQuantity.DoesNotExist:
            raise Http404
    def get(self, request, TigID, number, format=None):
        prod = ProductQuantity.objects.get(TigID=TigID)
        serialize = ProductQuantitySerializer(prod).data
        self.update_object(TigID, number + serialize['qte_stock'])
        update(TigID)
        prod = ProductQuantity.objects.get(TigID=TigID)
        serialize = ProductQuantitySerializer(prod).data
        return Response(serialize)

class Removesale(APIView):
    def update_object(self, TigID):
        try:
            ProductQuantity.objects.filter(TigID=TigID).update(sale=False)
        except ProductQuantity.DoesNotExist:
            raise Http404
    def get(self, request, TigID, format=None):
        self.update_object(TigID)
        prod = ProductQuantity.objects.get(TigID=TigID)
        return Response(ProductQuantitySerializer(prod).data)

class PutOnSale(APIView):
    def update_object(self, TigID, newprice):
        try:
            ProductQuantity.objects.filter(TigID=TigID).update(sale=True)
            ProductQuantity.objects.filter(TigID=TigID).update(discount=newprice)
        except ProductQuantity.DoesNotExist:
            raise Http404
    def get(self, request, TigID, newprice, format=None):
        try:
            value = float(newprice)
        except:
            raise Http404
        self.update_object(TigID, newprice)
        prod = ProductQuantity.objects.get(TigID=TigID)
        return Response(ProductQuantitySerializer(prod).data)

class DetailsInfoProduct(APIView):
    def get_object(self, TigID):
        try:
            return ProductQuantity.objects.get(TigID=TigID)
        except ProductQuantity.DoesNotExist:
            raise Http404
    def get(self, request, TigID, format=None):
        prod = self.get_object(TigID)
        serializer = ProductQuantitySerializer(prod)
        return Response(serializer.data)

class InfoProducts(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProductQuantity.objects.all():
            serializer = ProductQuantitySerializer(prod)
            res.append(serializer.data)
        return Response(res)


class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)

class RedirectionDetailProduit(APIView):
    def get_object(self, TigID):
        try:
            response = requests.get(baseUrl+'product/'+str(TigID)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
    def get(self, request, TigID, format=None):
        response = requests.get(baseUrl+'product/'+str(TigID)+'/')
        jsondata = response.json()
        return Response(jsondata)

class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProductInSale.objects.all():
            serializer = ProductInSaleSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['TigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)

class PromoDetail(APIView):
    def get_object(self, TigID):
        try:
            return ProductInSale.objects.get(TigID=TigID)
        except ProductInSale.DoesNotExist:
            raise Http404
    def get(self, request, TigID, format=None):
        prod = self.get_object(TigID)
        serializer = ProductInSaleSerializer(prod)
        response = requests.get(
            baseUrl+'product/'+str(serializer.data['TigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)

class ProductsListPerType(APIView):
    def get(self, request, format=None, category):
        products = []
        for product in Product.objects.all():
            serializer = ProductSerializer(product)
            if serializer.data['category'] == category
                products.append(serializer.data)
        return Response(products)