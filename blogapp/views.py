from django.shortcuts import render, get_object_or_404
from .models import Article


def blog_index(request):
    articles = Article.objects.all()
    return render(request, template_name="articles.html", context={"articles": articles})


def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, template_name="article_detail.html", context={"article": article})
