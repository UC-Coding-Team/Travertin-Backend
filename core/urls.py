from django.urls import path

from core.views.category import CategoryListCreateView, CategoryRetrieveUpdateDestroyView
from core.views.discount import DiscountListCreateView, DiscountRetrieveUpdateDestroyView
from core.views.outsite import NavbartexListCreateView, NavbartexRetrieveUpdateDestroyView
from core.views.product import ProductRetrieveUpdateDestroyView, ProductListCreateView

app_name = 'core'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount-retrieve-update-destroy'),
    path('navbartex/', NavbartexListCreateView.as_view(), name='navbartex-list-create'),
    path('navbartex/<int:pk>/', NavbartexRetrieveUpdateDestroyView.as_view(), name='navbartex-retrieve-update-destroy'),
]
