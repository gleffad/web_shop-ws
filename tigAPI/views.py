from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from tigAPI.models import Product as MProduct
from tigAPI.models import Transaction as MTransaction
from tigAPI.models import User as MUser
from tigAPI.serializers import ProductSerializer, TransactionSerializer, UserSerializer
from django.http import Http404, JsonResponse, HttpResponse
from datetime import datetime
import pandas as pd
from django.core import serializers
from rest_framework.permissions import IsAuthenticated

class Product(APIView):
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products = []
        for product in MProduct.objects.all():
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)


class FishProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products = []
        for product in MProduct.objects.filter(category=0):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)


class ShellfishProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products = []
        for product in MProduct.objects.filter(category=1):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)


class SeafoodProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products = []
        for product in MProduct.objects.filter(category=2):
            serializer = ProductSerializer(product)
            products.append(serializer.data)
        return Response(products)


class Transaction(APIView):
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        transactions = []
        for t in MTransaction.objects.all():
            serializer = TransactionSerializer(t)
            transactions.append(serializer.data)
        return Response(transactions)


class SetDiscount(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, format=None):
        tigID = request.data['tigID']
        discount = request.data['discount']
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


class ProductGroup(APIView):
    def decrement_stock(self, tigID, qty, operation):
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock - qty
        price = product[0].discount_price
        time_stamp = datetime.now()
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

    def set_discount(self, tigID, discount):
        product = MProduct.objects.filter(tigID=tigID)
        if discount != product[0].discount:
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

    def increment_stock(self, tigID, qty):
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock + qty
        time_stamp = datetime.now()
        price = product[0].producer_price * qty
        product.update(qty_stock=new_qty_stock)
        if product[0].discount_price == 0:
            product.update(discount=0)
            product.update(discount_price=product[0].retail_price)
        MTransaction.objects.create(
            tigID=tigID,
            date=time_stamp,
            price=price,
            quantity=qty,
            operation=0
        )

    def post(self, request, format=None):
        data = request.data
        for transaction in data:
            self.set_discount(transaction['tigID'], transaction['discount'])

            if transaction['stock'] != 0:
                print("------------------")
                print(transaction['operation'])
                print("------------------")
                if transaction['stock'] > 0:
                    self.increment_stock(transaction['tigID'], transaction['stock'])
                elif transaction['stock'] < 0:
                    self.decrement_stock(transaction['tigID'], transaction['stock'] * (-1), transaction['operation'])

        return Response([])


class DecrementStock(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        tigID = request.data['tigID']
        qty = request.data['qty']
        operation = request.data['operation']
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock - qty
        price = product[0].discount_price
        time_stamp = datetime.now()
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
    permission_classes = (IsAuthenticated,)

    def patch(self, request, format=None):
        tigID = request.data['tigID']
        qty = request.data['qty']
        product = MProduct.objects.filter(tigID=tigID)
        new_qty_stock = product[0].qty_stock + qty
        time_stamp = datetime.now()
        price = product[0].producer_price * qty
        product.update(qty_stock=new_qty_stock)
        if product[0].discount_price == 0:
            product.update(discount=0)
            product.update(discount_price=product[0].retail_price)
        MTransaction.objects.create(
            tigID=tigID,
            date=time_stamp,
            price=price,
            quantity=qty,
            operation=1
        )
        serialized = ProductSerializer(product.get())
        return Response(serialized.data)


class OnSaleProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        on_sale_products = MProduct.objects.filter(on_sale=True)
        serialized = ProductSerializer(on_sale_products.get())
        return Response(serialized.data)


class CustomComptability(APIView):
    permission_classes = (IsAuthenticated,)

    def tranform_date(self, t):
        return datetime.strptime(t["date"], "%Y-%m-%dT%H:%M:%S.%fZ")

    def tranform_dollars(self, t):
        return t["quantity"] * t["price"]

    def post(self, request, fromat=None):
        product_type = request.data['product_type']
        time_format = request.data['time_format']

        iter = MProduct.objects.all()

        if product_type == "fish":
            iter = MProduct.objects.filter(category=0)
        elif product_type == "shellfish":
            iter = MProduct.objects.filter(category=1)
        elif product_type == "seafood":
            iter = MProduct.objects.filter(category=2)

        produits = []

        for product in iter:
            serializer = ProductSerializer(product)
            produits.append(serializer.data['tigID'])

        transactions = []
        qs = MTransaction.objects.filter(tigID__in=produits, operation=1)

        if not qs:
            return Response([])

        for transaction in qs:
            serializer = TransactionSerializer(transaction)
            transactions.append(serializer.data)

        data = {
            "datetime": list(map(self.tranform_date, transactions)),
            "dollars": list(map(self.tranform_dollars, transactions))
        }

        df = pd.DataFrame(data)

        result = []
        if time_format == "day":
            result = df.groupby(pd.Grouper(
                key='datetime', freq='D')).sum().reset_index()
        elif time_format == "month":
            result = df.groupby(pd.Grouper(
                key='datetime', freq='M')).sum().reset_index()
        elif time_format == "year":
            result = df.groupby(pd.Grouper(
                key='datetime', freq='Y')).sum().reset_index()
        else:
            raise Http404

        res = []
        for i in range(0, result.shape[0]):
            res.append({
                "date": str(result.datetime[i]),
                "revenues": result.dollars[i]
            })

        return Response(res)
