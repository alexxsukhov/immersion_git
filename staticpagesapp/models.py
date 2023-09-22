from django.db import models


class StaticPage(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", default="")
    slug = models.SlugField(unique=True, verbose_name="Символьный код", default="")
    image = models.ImageField(upload_to='static/images/', default="", blank=True)
    h1 = models.CharField(max_length=150, verbose_name="Заголовок H1", default="", blank=True)
    announce = models.TextField(max_length=500, verbose_name="Краткое описание", default="", blank=True)
    description = models.TextField(max_length=10000, verbose_name="Описание", default="", blank=True)
    seo_title = models.CharField(max_length=150, verbose_name="Seo Title", default="", blank=True)
    seo_description = models.TextField(max_length=500, verbose_name="Seo Description", default="", blank=True)
    seo_keywords = models.CharField(max_length=100, verbose_name="Seo Keywords", default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
