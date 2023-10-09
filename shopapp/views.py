from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from ordersapp.models import Order, Client
from .forms import EditProduct
from .models import Product, Category


def index_shop(request):
    categories = Category.objects.all().filter(parent=None).order_by('name')
    return render(request, template_name="shop.html", context={"categories": categories})


def detail_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, template_name="product_detail.html", context={"product": product})


def detail_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.filter(parent_id=category.pk)
    products = Product.objects.filter(category_id=category.pk)
    return render(request, template_name="detail_category.html",
                  context={"categories": categories,
                           "products": products,
                           "category": category})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = EditProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'product_edit.html', {'form': form})

    else:
        form = EditProduct(instance=product)

    return render(request, 'product_edit.html', {'form': form})
