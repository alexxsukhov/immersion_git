from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="")
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="")
    description = models.TextField(max_length=10000, verbose_name="Описание", default="")
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="")
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="")
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="")
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="")
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
