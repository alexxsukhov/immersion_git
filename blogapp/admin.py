from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    ordering = ("pk", "name")
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    list_per_page = 1


admin.site.register(Article, ArticleAdmin)
