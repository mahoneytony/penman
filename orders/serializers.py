from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=300)
    topic = serializers.CharField(max_length=1000)
