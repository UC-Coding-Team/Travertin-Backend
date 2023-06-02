from pytz import timezone
from rest_framework import serializers
from datetime import datetime, time

from core.models.outsite import Navbartex


class NavbartexSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Navbartex
        fields = ('id', 'status', 'text')

    def get_status(self, obj):
        current_time = datetime.now(timezone('Asia/Tashkent')).time()
        # current_time = time(21, 0)

        if obj.start_time <= current_time <= obj.end_time:
            return 'green'
        else:
            return 'red'
