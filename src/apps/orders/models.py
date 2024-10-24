from django.db import models


class Order(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, related_name='orders')
    customer = models.ForeignKey('customers.Customer', on_delete=models.SET_NULL, null=True, related_name='orders')

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)