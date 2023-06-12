from django.urls import path

from core.views.discount import DiscountListCreateView, DiscountRetrieveUpdateDestroyView
from core.views.outsite import NavbartexListCreateView, NavbartexRetrieveUpdateDestroyView
from core.views.category import CategoryListCreateView
from core.views.product import (
    ProductRetrieveView,
    CategoryProductListView,
    ProductListView,
)


app_name = 'core'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category_list'),
    path('products/<int:pk>/', ProductRetrieveView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categories/<int:pk>/', CategoryProductListView.as_view(), name='category_product_list'),
    path('discounts/', DiscountListCreateView.as_view(), name='discount_list_create'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount_retrieve_update_destroy'),
    path('navbartex/', NavbartexListCreateView.as_view(), name='navbartex_list_create'),
    path('navbartex/<int:pk>/', NavbartexRetrieveUpdateDestroyView.as_view(), name='navbartex_retrieve_update_destroy'),
]
