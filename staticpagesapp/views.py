from django.shortcuts import render
from .models import StaticPage


# Create your views here.
def index(request):
    index_info = StaticPage.objects.get(id=1)
    return render(request, template_name="index.html", context={"index_info": index_info})


def about(request):
    return render(request, template_name="about.html")
