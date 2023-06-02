from rest_framework import generics
from core.models import Discount
from core.serializers.discount import DiscountSerializer


class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    http_method_names = ['get']

class DiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    http_method_names = ['get']