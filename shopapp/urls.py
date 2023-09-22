from django.urls import path

from shopapp import views

urlpatterns = [
    path('slug', views.product_slug, name='product_slug'),
]
