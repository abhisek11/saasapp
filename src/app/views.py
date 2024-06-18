from django.http import HttpResponse
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent
print(this_dir)

def home_page_view(request, *args,**kwargs):
    print(this_dir)
    return HttpResponse("<h1> hello world</h1>")
