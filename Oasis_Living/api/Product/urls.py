
from django.urls import path, include
from .views import ProductListView, ProductDetailsView, RetrieveProductsbySKUView, AvailableProductsView, SoldoutProductsView, QuantityUpdateView
# from .views import ProductListViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', ProductListViewSet, basename='products')

urlpatterns = [
    # path('', include(router.urls))
    path('', ProductListView.as_view()),
    path('<int:id>/', ProductDetailsView.as_view()),
    path('availableProducts/', AvailableProductsView.as_view()),
    path('SKU/<str:SKU>/', RetrieveProductsbySKUView.as_view()),
    path('soldout/', SoldoutProductsView.as_view()),
    path('qtyUpdate/<str:SKU>/', QuantityUpdateView.as_view())
]
