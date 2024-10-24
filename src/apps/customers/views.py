from rest_framework.views import APIView
from rest_framework.response import Response

from apps.customers.models import Customer


class AllProductsOrderingCustomer(APIView):

    def get(self, request):
        customers = Customer.objects.all().prefetch_related('orders', 'orders__product')
        data = {}
        for customer in customers:
            customer_orders = customer.orders.all()
            data = {
                customer.id:[]
            }
            for order in customer_orders:
                order_data = {
                    'product_id': order.product.id,
                    'product_name': order.product.name,
                    'product_price': order.product.price,
                }
                data[customer.id].append(order_data)

        return Response(data)
    

class SumCountsBuyedProducts(APIView):

    def get(self, request):
        customers = Customer.objects.all().prefetch_related('orders', 'orders__product')
        data = {}
        for customer in customers:
            customer_orders = customer.orders.all()
            data[customer.id] = {'buy_products':0, 'buy_products_price':0}
            for order in customer_orders:
                data[customer.id]['buy_products_price'] += order.product.price
                data[customer.id]['buy_products'] += 1

        return Response(data)