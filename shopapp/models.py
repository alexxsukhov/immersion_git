from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="")
    parent = models.ForeignKey('self', verbose_name="Родитель", null=True, blank=True, on_delete=models.CASCADE)
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="")
    description = models.TextField(max_length=10000, verbose_name="Описание", default="")
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="")
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="")
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="")
    image = models.ImageField(upload_to='static/images/products/', default="", blank=True)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="", blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2, null=False, blank=False)
    category_id = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.SET_DEFAULT, default="")
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="", blank=True)
    description = models.TextField(verbose_name="Описание", default="", blank=True)
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="", blank=True)
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="", blank=True)
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия", default="")
    phone = models.CharField(max_length=15, verbose_name="Телефон", default="")
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300, verbose_name="Адрес", default="")
    date_registration = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.client.last_name} {self.client.first_name} on {self.order_date}"
    

