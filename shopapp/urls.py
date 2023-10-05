from django.urls import path

from shopapp import views

urlpatterns = [
    path('', views.index_shop, name='index_shop'),
    path('product/<slug:slug>/', views.detail_product, name='detail_product'),
    path('category/<slug:slug>/', views.detail_category, name='detail_category'),
]
