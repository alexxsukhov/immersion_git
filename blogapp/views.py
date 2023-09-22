from django.shortcuts import render, get_object_or_404
import logging
from .models import Article

logger = logging.getLogger(__name__)


def blog_index(request):
    logger.info('Это информационное сообщение')
    articles = Article.objects.all()
    return render(request, template_name="articles.html", context={"articles": articles})


def blog_detail(request, slug):
    logger.info('Это информационное сообщение')
    article = get_object_or_404(Article, slug=slug)
    return render(request, template_name="article_detail.html", context={"article": article})
