from rest_framework import serializers

from core.models.outsite import Navbartex


class NavbartexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbartex
        fields = ('id', 'status', 'text')
        read_only_fields = ('id',)

    def validate_status(self, value):
        # Add custom validation logic for the status field if needed
        # Ensure the status meets your requirements and return the value
        return value