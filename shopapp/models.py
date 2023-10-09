from django.db import models
from django.db.models import JSONField
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="", blank=True)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="")
    parent = models.ForeignKey('self', verbose_name="Родитель", null=True, blank=True, on_delete=models.CASCADE)
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="")
    description = models.TextField(max_length=10000, verbose_name="Описание", default="")
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="")
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="")
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="", blank=True)
    image = models.ImageField(upload_to='static/images/products/', default="", blank=True)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="", blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2, null=False, blank=False)
    category_id = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.SET_DEFAULT, default="")
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="", blank=True)
    description = models.TextField(verbose_name="Описание", default="", blank=True)
    characteristics = JSONField(default=list, verbose_name="Характеристики")
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="", blank=True)
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="", blank=True)
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
