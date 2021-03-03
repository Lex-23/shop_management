from rest_framework import serializers
from management.models import (Category,
                               Product,
                               Stock,
                               Store,
                               ProdStock,
                               OrderStore)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id', 'name', 'description', 'url',


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('category_name',
                  'category',
                  'id',
                  'name',
                  'description',
                  'url')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = 'id', 'name', 'description', 'url',


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = 'id', 'name', 'description', 'url',


class ProdStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdStock
        fields = ('id',
                  'unique_number',
                  'stock',
                  'stock_name',
                  'product',
                  'position_info',
                  'balance',
                  'url')


class OrderStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderStore
        fields = ('id',
                  'store',
                  'store_name',
                  'order',
                  'order_info',
                  'count',
                  'url')
