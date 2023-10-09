from django.db import models

from shopapp.models import Product


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия", default="")
    password = models.CharField(max_length=50, verbose_name="Пароль", default="")
    phone = models.CharField(max_length=15, verbose_name="Телефон", default="")
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=300, verbose_name="Адрес", default="")
    date_registration = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "покупателя"
        verbose_name_plural = "покупатели"


class Order(models.Model):
    client = models.ForeignKey(Client, verbose_name="Пользователь", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name="Товары")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def get_products(self):
        return ", ".join(str(product) for product in self.products.all())

    get_products.short_description = 'Товары'

    def __str__(self):
        return f"Order by {self.client.last_name} {self.client.first_name} on {self.order_date}"

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
