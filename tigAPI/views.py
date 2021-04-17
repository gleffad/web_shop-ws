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
class DecrementStock(APIView):
    def update_object(self, pk, number):
        try:
            ProductQuantity.objects.filter(
                pk=pk).update(quantityInStock=number)
        except ProductQuantity.DoesNotExist:
            raise Http404

    def get(self, request, pk, number, format=None):
        prod = ProductQuantity.objects.get(pk=pk)
        serialize = ProductQuantitySerializer(prod).data
        quantityInStock = serialize['quantityInStock'] - number

        if quantityInStock >= 0:
            self.update_object(pk, quantityInStock)
        else:
            raise Http404

        update(pk)
        prod = ProductQuantity.objects.get(pk=pk)
        serialize = ProductQuantitySerializer(prod).data

        return Response(serialize)


class IncrementStock(APIView):
    def update_object(self, pk, number):
        try:
            ProductQuantity.objects.filter(
                pk=pk).update(quantityInStock=number)
        except ProductQuantity.DoesNotExist:
            raise Http404

    def get(self, request, pk, number, format=None):
        prod = ProductQuantity.objects.get(pk=pk)
        serialize = ProductQuantitySerializer(prod).data
        self.update_object(pk, number + serialize['quantityInStock'])

        update(pk)
        prod = ProductQuantity.objects.get(pk=pk)
        serialize = ProductQuantitySerializer(prod).data

        return Response(serialize)


class Removesale(APIView):
    def update_object(self, pk):
        try:
            ProductQuantity.objects.filter(pk=pk).update(sale=False)
        except ProductQuantity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.update_object(pk)
        prod = ProductQuantity.objects.get(pk=pk)
        return Response(ProductQuantitySerializer(prod).data)


class PutOnSale(APIView):
    def update_object(self, pk, newprice):
        try:
            ProductQuantity.objects.filter(pk=pk).update(sale=True)
            ProductQuantity.objects.filter(pk=pk).update(discount=newprice)
        except ProductQuantity.DoesNotExist:
            raise Http404

    def get(self, request, pk, newprice, format=None):
        try:
            value = float(newprice)
        except:
            raise Http404

        self.update_object(pk, newprice)
        prod = ProductQuantity.objects.get(pk=pk)

        return Response(ProductQuantitySerializer(prod).data)


class DetailsInfoProduct(APIView):
    def get_object(self, pk):
        try:
            return ProductQuantity.objects.get(pk=pk)
        except ProductQuantity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
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
    def get_object(self, pk):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        response = requests.get(baseUrl+'product/'+str(pk)+'/')
        jsondata = response.json()
        return Response(jsondata)


class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProductInSale.objects.all():
            serializer = ProductInSaleSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)


class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductInSale.objects.get(pk=pk)
        except ProductInSale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductInSaleSerializer(prod)
        response = requests.get(
            baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
