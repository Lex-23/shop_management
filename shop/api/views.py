from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from management.models import (Category,
                               Product,
                               Stock,
                               Store,
                               ProdStock,
                               OrderStore)
from .serializers import (CategorySerializer,
                          ProductSerializer,
                          StockSerializer,
                          StoreSerializer,
                          ProdStockSerializer,
                          OrderStoreSerializer)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name']
    search = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name', 'category']
    search_fields = ['name']
    search = ['name']
    ordering_fields = ['name', 'category']
    ordering = ['name', 'category']


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name']
    search = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name']
    search = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class ProdStockViewSet(viewsets.ModelViewSet):
    queryset = ProdStock.objects.all()
    serializer_class = ProdStockSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['stock', 'product']
    search_fields = ['unique_number']
    search = ['unique_number']
    ordering_fields = ['product', 'stock']
    ordering = ['stock', 'product']


class OrderStoreViewSet(viewsets.ModelViewSet):
    queryset = OrderStore.objects.all()
    serializer_class = OrderStoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['store']
    search_fields = ['order']
    search = ['order']
    ordering_fields = ['store']
    ordering = ['store']
