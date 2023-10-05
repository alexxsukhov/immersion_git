from django.shortcuts import render, get_object_or_404
import logging
from .models import Article

logger = logging.getLogger(__name__)


def blog_index(request):
    articles = Article.objects.all().order_by('-date')

    count_articles = 5
    start_index = 0
    end_index = count_articles
    end_page = (len(articles) // count_articles) + 1
    range_pages = (1, end_page)
    current_page = 1

    if request.GET.get('page'):
        current_page = int(request.GET.get('page'))
        start_index = (current_page - 1) * count_articles
        end_index = current_page * count_articles

    elif request.GET.get('show_all') == "Y":
        start_index = 0
        end_index = len(articles)

    list_articles = articles[start_index:end_index]
    return render(request, template_name="articles.html", context={"articles": list_articles,
                                                                   "range_pages": range_pages,
                                                                   "current_page": current_page,
                                                                   "end_page": end_page,
                                                                   "show_all": request.GET.get('show_all')})


def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    return render(request, template_name="article_detail.html", context={"article": article})
