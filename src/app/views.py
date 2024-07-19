from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args,**kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args,**kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My home page"
    html_template = "home.html"
    try:
        percent = (page_qs.count() * 100)/ qs.count()
    except:
        percent = 0
    context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, context)
