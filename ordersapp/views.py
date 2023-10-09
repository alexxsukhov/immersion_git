from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Order, Client


def products_in_date_range(request, days, client_id):
    current_client = Client.objects.filter(pk=client_id).first()
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    orders = Order.objects.filter(client=current_client, order_date__range=(start_date, end_date))

    products = set()
    for order in orders:
        products.update(order.products.all())

    context = {
        'products': products,
        'days': days,
    }

    return render(request, 'products_in_date_range.html', context)
