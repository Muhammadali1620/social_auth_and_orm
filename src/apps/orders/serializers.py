from rest_framework import serializers

from apps.orders.models import Order


class OrderSerializer(serializers.Serializer):
    from_created = serializers.DateField()
    to_created = serializers.DateField()

    def save(self, **kwargs):
        orders = Order.objects.filter(
            created_at__range=(self.validated_data['from_created'], self.validated_data['to_created'])
        )
        self.validated_data['orders'] = orders.values('id', 'created_at', 'total_price')