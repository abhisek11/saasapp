from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args,**kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My home page"
    context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100)/ qs.count(),
        "total_visit_count": qs.count()
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, context)


def my_old_home_page_view(request, *args,**kwargs):
    print(this_dir)
    my_title = "My home page"
    context = {
        "page_title": my_title
    }
    html_ = """<!DOCTYPE html>
                <html>
                    <body>
                        <h1>This is my {page_title} first page</h1>
                    </body>
                </html>""".format(**context)
    # html_file_path = this_dir /"home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)