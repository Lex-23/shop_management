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
    name = models.CharField(unique=True, max_length=200, verbose_name='product')
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def category_name(self):
        return self.category.name


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
        return f'{self.product} #{str(self.unique_number)}'

    def position_info(self):
        return f'{self.product.name}/{self.product.category.name}'

    def stock_name(self):
        return self.stock.name


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

    def store_name(self):
        return self.store.name

    def order_info(self):
        return (f'#{self.order.unique_number} '
                f'product:{self.order.product.name}/'
                f'{self.order.product.category.name}')

    def count_after_sale(self, sale_count):
        self.count -= sale_count

    def count_after_delivery(self, delivery_count):
        self.count += delivery_count

    def __str__(self):
        return f'{self.store} have {self.order}: {self.count} pcs'
