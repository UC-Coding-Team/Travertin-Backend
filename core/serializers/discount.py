from rest_framework import serializers
from core.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'title', 'text', 'image', 'url')
        read_only_fields = ('id',)

    def validate_image(self, value):
        # Add custom validation logic for the image field if needed
        # Ensure the image meets your requirements and return the value
        return value