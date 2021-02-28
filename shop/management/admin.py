from django.contrib import admin

from .models import Category, Product, Store


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


class StoreAdmin(admin.ModelAdmin):
    fields = 'name', 'product',
    search_fields = 'name', 'product',
    list_display = 'name', 'id',
    list_filter = 'name', 'product',


admin.site.register(Store, StoreAdmin)
