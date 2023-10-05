from django.contrib import admin
from .models import Product, Category, Client


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_name', 'first_name', 'phone', 'email')


admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
