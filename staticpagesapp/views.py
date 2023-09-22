import logging

from django.shortcuts import render
from .models import StaticPage

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info('Это информационное сообщение')
    index_info = StaticPage.objects.get(id=1)
    return render(request, template_name="index.html", context={"index_info": index_info})


def about(request):
    logger.info('Это информационное сообщение')
    about_info = StaticPage.objects.get(id=2)
    return render(request, template_name="about.html", context={"about_info": about_info})
