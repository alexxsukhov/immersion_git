from django.shortcuts import render
from django.http import HttpResponse


def product_slug(request):
    return HttpResponse('product')