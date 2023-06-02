from django.urls import path

from core.views.discount import DiscountListCreateView, DiscountRetrieveUpdateDestroyView
from core.views.outsite import NavbartexListCreateView, NavbartexRetrieveUpdateDestroyView
from core.views.category import CategoryListCreateView
from core.views.product import (
    ProductRetrieveView,
    CategoryProductListView
)


app_name = 'core'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('products/<int:pk>/', ProductRetrieveView.as_view(), name='product-detail'),
    path('categories/<int:pk>/', CategoryProductListView.as_view(), name='category-product-list'),
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount-retrieve-update-destroy'),
    path('navbartex/', NavbartexListCreateView.as_view(), name='navbartex-list-create'),
    path('navbartex/<int:pk>/', NavbartexRetrieveUpdateDestroyView.as_view(), name='navbartex-retrieve-update-destroy'),
]
