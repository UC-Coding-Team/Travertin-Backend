from rest_framework import generics
from rest_framework.response import Response

from core.models import Product, Category
from core.serializers.product import ProductSerializer, ProductDetailSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryProductListView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        products = Product.objects.filter(category=instance)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

