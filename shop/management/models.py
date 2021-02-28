from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products')
    name = models.CharField(max_length=200, verbose_name='product')
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Stock(models.Model):
    """модель Склады"""
    name = models.CharField(max_length=200, verbose_name='stock_name')
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Stock'

    def __str__(self):
        return self.name


class ProdStock(models.Model):
    """модель наличия товара на складе, каждая строка - уникальная"""
    unique_number = models.PositiveIntegerField(unique=True)
    stock = models.ForeignKey(Stock,
                              on_delete=models.DO_NOTHING,
                              related_name='stocks_prod')
    product = models.ForeignKey(Product,
                                on_delete=models.DO_NOTHING,
                                related_name='products_stock')
    balance = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ('stock', 'product')
        verbose_name = 'Products_in_stock'

    def __str__(self):
        return str(self.unique_number)


class Store(models.Model):
    """модель Магазины"""
    name = models.CharField(max_length=200, verbose_name='store_name')
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Store'

    def __str__(self):
        return self.name


class OrderStore(models.Model):
    """модель поступления товара в магазин со склада"""
    store = models.ForeignKey(Store, on_delete=models.CASCADE,
                              related_name='stores')
    order = models.OneToOneField(ProdStock, on_delete=models.DO_NOTHING,
                                 related_name='orders')
    count = models.PositiveBigIntegerField(default=0)


