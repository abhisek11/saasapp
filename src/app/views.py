from django.http import HttpResponse
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent
print(this_dir)

def home_page_view(request, *args,**kwargs):
    print(this_dir)
    html_ = """<!DOCTYPE html>
                <html>
                    <body>
                        <h1>This is my first page</h1>
                    </body>
                </html>"""
    # html_file_path = this_dir /"home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
