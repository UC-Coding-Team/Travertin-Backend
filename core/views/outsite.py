from rest_framework import generics
from core.models.outsite import Navbartex
from core.serializers.outsite import NavbartexSerializer
from datetime import datetime, time


class NavbartexListCreateView(generics.ListCreateAPIView):
    queryset = Navbartex.objects.all()
    serializer_class = NavbartexSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        now = datetime.now().time()
        if time(9, 0) <= now <= time(18, 0):
            context['tochka_color'] = 'green'
        else:
            context['tochka_color'] = 'red'
        return context


class NavbartexRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Navbartex.objects.all()
    serializer_class = NavbartexSerializer