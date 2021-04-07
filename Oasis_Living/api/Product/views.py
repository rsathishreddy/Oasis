from django.shortcuts import render

from .models import Product

from .serializers import ProductSerializer

# from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins

from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.


class ProductListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProductDetailsView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


class RetrieveProductsbySKUView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'SKU'

    def get(self, request, SKU):
        return self.retrieve(request, SKU=SKU)


class AvailableProductsView(generics.ListAPIView, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'availableProducts'

    def get_queryset(self):
        return Product.objects.filter(Qty__gt=0)


class SoldoutProductsView(generics.ListAPIView, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'soldout'

    def get_queryset(self):
        return Product.objects.filter(Qty=0)


class QuantityUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'SKU'

    def put(self, request, SKU):
        return self.update(request, SKU=SKU)
