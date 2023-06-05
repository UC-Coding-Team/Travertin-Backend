from rest_framework import generics

from core.models import Category
from core.serializers.category import CategorySerializer


class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

