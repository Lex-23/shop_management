from django.contrib import admin

from .models import (Category, Product, Stock,
                     ProdStock, Store, OrderStore)


class CategoryAdmin(admin.ModelAdmin):
    fields = 'name', 'description',
    search_fields = 'name',
    list_display = 'name', 'id',
    list_filter = 'name',


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = 'name', 'description', 'category',
    search_fields = 'name', 'category',
    list_display = 'name', 'id', 'category',
    list_filter = 'name', 'category',


admin.site.register(Product, ProductAdmin)


class StockAdmin(admin.ModelAdmin):
    fields = 'name', 'description',
    search_fields = 'name',
    list_display = 'name', 'id',
    list_filter = 'name',


admin.site.register(Stock, StockAdmin)


class ProdStockAdmin(admin.ModelAdmin):
    fields = 'unique_number', 'stock', 'product', 'balance',
    search_fields = 'stock', 'product', 'unique_number'
    list_display = 'id', 'unique_number', 'stock', 'product', 'balance',
    list_filter = 'stock', 'product',


admin.site.register(ProdStock, ProdStockAdmin)


class StoreAdmin(admin.ModelAdmin):
    fields = 'name', 'description',
    search_fields = 'name',
    list_display = 'name', 'id',
    list_filter = 'name',


admin.site.register(Store, StoreAdmin)


class OrderStoreAdmin(admin.ModelAdmin):
    fields = 'store', 'order', 'count',
    search_fields = 'store', 'order',
    list_display = 'id', 'store', 'order', 'count',
    list_filter = 'store',


admin.site.register(OrderStore, OrderStoreAdmin)
