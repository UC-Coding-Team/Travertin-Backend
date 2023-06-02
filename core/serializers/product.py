from rest_framework import serializers

from core.models import Category, Product
from core.serializers.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_id', 'price', 'slug', 'image']
        read_only_fields = ['id', 'slug', 'image']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'slug', 'image']
        read_only_fields = ['id', 'slug', 'image']
