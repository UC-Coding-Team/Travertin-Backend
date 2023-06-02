from django.urls import path

from core.views.category import CategoryListCreateView, CategoryRetrieveUpdateDestroyView
from core.views.product import ProductRetrieveUpdateDestroyView, ProductListCreateView

app_name = 'core'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
