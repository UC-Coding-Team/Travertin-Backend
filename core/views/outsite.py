from rest_framework import generics,response
from pytz import timezone
from core.models.outsite import Navbartex
from core.serializers.outsite import NavbartexSerializer
from datetime import datetime, time


class NavbartexListCreateView(generics.ListCreateAPIView):
    serializer_class = NavbartexSerializer
    http_method_names = ['get']

    def get_queryset(self):
        current_time = datetime.now(timezone('Asia/Tashkent')).time()
        # current_time = time(21, 0)


        if current_time >= Navbartex.objects.first().start_time and current_time <= Navbartex.objects.first().end_time:
            queryset = Navbartex.objects.filter(status='green')
        else:
            queryset = Navbartex.objects.filter(status='red')

        return queryset


class NavbartexRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Navbartex.objects.all()
    serializer_class = NavbartexSerializer
    http_method_names = ['get']