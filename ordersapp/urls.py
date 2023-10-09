from django.urls import path

from ordersapp import views

urlpatterns = [
    path('<int:client_id>/<int:days>/', views.products_in_date_range, name='products_in_range_date'),
]