from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from tigAPI.models import Product as MProduct
from tigAPI.models import Transaction as MTransaction
from tigAPI.models import User as MUser
from tigAPI.serializers import ProductSerializer, TransactionSerializer, UserSerializer
from django.http import Http404, JsonResponse, HttpResponse
import time

class ProductFish(APIView):
    def get(self, request, format=None) :
        products = []
        for product in MProduct.objects.filter(category=0):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)

class ProductShellfish(APIView):
    def get(self, request, format=None) :
        products = []
        for product in MProduct.objects.filter(category=1):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)

class ProductSeafood(APIView):
    def get(self, request, format=None) :
        products = []
        for product in MProduct.objects.filter(category=2):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)

class Product(APIView):
    def get_object(self, tigID):
        try:
            return MProduct.objects.get(tigID=tigID)
        except:
            raise Http404

    def get(self, request, tigID, format=None):
        product = self.get_object(tigID)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductList(APIView):
    def get(self, request, format=None):
        products = []
        for product in MProduct.objects.all():
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)


class Transaction(APIView):
    def get_object(self, tigID):
        try:
            return MTransaction.objects.get(tigID=tigID)
        except:
            raise Http404

    def get(self, request, tigID, format=None):
        transaction = self.get_object(tigID)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)


class TransactionList(APIView):
    def get(self, request, format=None):
        transactions = []
        for t in MTransaction.objects.all():
            serializer = TransactionSerializer(t)
            transactions.append(serializer.data)
        return Response(transactions)


class SetDiscount(APIView):

    def patch(self, request, format=None):
        # ----------------------------------------
        tigID = request.data['tigID']
        discount = request.data['discount']
        # ----------------------------------------
        product = MProduct.objects.filter(tigID=tigID)
        price = product[0].retail_price - \
            ((discount*product[0].retail_price)/100)
        if discount >= 0 and discount <= 100:
            product.update(discount=discount)
            product.update(discount_price=price)
            if discount == 0:
                product.update(on_sale=False)
            else:
                product.update(on_sale=True)
        else:
            raise Http404
        serialized = ProductSerializer(product.get())
        return Response(serialized.data)


class DecrementStock(APIView):
    def get(self, request, tigID, qty, operation, format=None):
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock - qty
        price = product[0].discount_price
        time_stamp = time.ctime()
        if new_qty_stock >= 0:
            product.update(qty_stock=new_qty_stock)
            if operation == 1:
                MTransaction.objects.create(
                    tigID=tigID,
                    date=time_stamp,
                    price=price,
                    quantity=qty,
                    operation=operation
                )
            elif operation == 2:
                MTransaction.objects.create(
                    tigID=tigID,
                    date=time_stamp,
                    price=0,
                    quantity=qty,
                    operation=operation
                )
            else:
                raise Http404
        else:
            raise Http404
        serialized = ProductSerializer(product.get())
        return Response(serialized.data)


class IncrementStock(APIView):
    def patch(self, request, format=None):
        # ----------------------------------------
        tigID = request.data['tigID']
        qty = request.data['qty']
        # ----------------------------------------
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock + qty
        time_stamp = time.ctime()
        price = product[0].producer_price * qty
        product.update(qty_stock=new_qty_stock)
        MTransaction.objects.create(
            tigID=tigID,
            date=time_stamp,
            price=price,
            quantity=qty,
            operation=2
        )
        serialized = ProductSerializer(product.get())
        return Response(serialized.data)


class OnSaleProductList(APIView):
    def get(self, request, format=None):
        on_sale_products = MProduct.objects.filter(on_sale=True)
        serialized = ProductSerializer(on_sale_products.get())
        return Response(serialized.data)


'''
class Removesale(APIView):
    def update_object(self, tigID):
        try:
            MProduct.objects.filter(tigID=tigID).update(sale=False)
        except MProduct.DoesNotExist:
            raise Http404
    def get(self, request, tigID, format=None):
        self.update_object(tigID)
        prod = MProduct.objects.get(tigID=tigID)
        return Response(ProductSerializer(prod).data)

class PutOnSale(APIView):
    def update_object(self, tigID, newprice):
        try:
            MProduct.objects.filter(tigID=tigID).update(sale=True)
            MProduct.objects.filter(tigID=tigID).update(discount=newprice)
        except MProduct.DoesNotExist:
            raise Http404
    def get(self, request, tigID, newprice, format=None):
        try:
            value = float(newprice)
        except:
            raise Http404
        self.update_object(tigID, newprice)
        prod = MProduct.objects.get(tigID=tigID)
        return Response(ProductSerializer(prod).data)

class DetailsInfoProduct(APIView):
    def get_object(self, tigID):
        try:
            return MProduct.objects.get(tigID=tigID)
        except MProduct.DoesNotExist:
            raise Http404
    def get(self, request, tigID, format=None):
        prod = self.get_object(tigID)
        serializer = ProductSerializer(prod)
        return Response(serializer.data)

class InfoProducts(APIView):
    def get(self, request, format=None):
        res = []
        for prod in MProduct.objects.all():
            serializer = ProductSerializer(prod)
            res.append(serializer.data)
        return Response(res)


class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)

class RedirectionDetailProduit(APIView):
    def get_object(self, tigID):
        try:
            response = requests.get(baseUrl+'product/'+str(tigID)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
    def get(self, request, tigID, format=None):
        response = requests.get(baseUrl+'product/'+str(tigID)+'/')
        jsondata = response.json()
        return Response(jsondata)


class PromoDetail(APIView):
    def get_object(self, tigID):
        try:
            return ProductInSale.objects.get(tigID=tigID)
        except ProductInSale.DoesNotExist:
            raise Http404
    def get(self, request, tigID, format=None):
        prod = self.get_object(tigID)
        serializer = ProductInSaleSerializer(prod)
        response = requests.get(
            baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)

class ProductListPerType(APIView):
    def get(self, request, format=None, category):
        return Response(TransactionSerializer(MTransaction.objects.filter(tigID=tigID))).data)
'''
