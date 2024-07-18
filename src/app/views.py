from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args,**kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My home page"
    context = {
        "page_title": my_title,
        "queryset": queryset,
    }
    html_template = "home.html"
    PageVisit.objects.create()
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