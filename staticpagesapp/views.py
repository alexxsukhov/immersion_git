from django.shortcuts import render
from .models import StaticPage


# Create your views here.
def index(request):
    index_info = StaticPage.objects.get(id=1)
    return render(request, template_name="index.html", context={"index_info": index_info})


def about(request):
    about_info = StaticPage.objects.get(id=2)
    return render(request, template_name="about.html", context={"about_info": about_info})
