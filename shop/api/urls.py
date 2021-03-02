from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,
                    ProductViewSet,
                    StockViewSet,
                    StoreViewSet,
                    ProdStockViewSet,
                    OrderStoreViewSet)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"stocks", StockViewSet)
router.register(r"stores", StoreViewSet)
router.register(r"prod_in_stocks", ProdStockViewSet)
router.register(r"order_in_stores", OrderStoreViewSet)

urlpatterns = [path("", include(router.urls))]
