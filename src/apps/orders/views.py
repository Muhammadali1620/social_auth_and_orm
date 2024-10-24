from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.orders.serializers import OrderSerializer


class OrderListAPIView(GenericAPIView):
    queryset = []
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.validated_data, status=200)