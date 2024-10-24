from django.urls import path
from apps.customers import views


urlpatterns = [
    path('', views.AllProductsOrderingCustomer.as_view()),
    path('orders_count/', views.SumCountsBuyedProducts.as_view()),
]