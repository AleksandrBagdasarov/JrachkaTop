from api.models import Order
from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.Serializer):
    point_id = serializers.IntegerField()
    order = OrderItemSerializer(many=True)


class ShowOrderSerializer(serializers.ModelSerializer):
    class Meta:

        model = Order
        # fields = "__all__"
        exclude = ("user",)
