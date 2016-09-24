from django.http import HttpResponse
from django.template import loader
from .helper import handle_uploaded_text_file, handle_uploaded_pdf_file


def index(request):
    template = loader.get_template('Website/index.html')
    return HttpResponse(template.render({'text': 'sa'}, request))

def upload_file(request):
    template = loader.get_template('Website/index.html')
    if request.method == 'POST':
        f = request.FILES['fileToUpload']
        if f.name[-3:] == "pdf":
            t = handle_uploaded_pdf_file(f)
        else:
            t = handle_uploaded_text_file(f)
        return HttpResponse(template.render({'text': t}, request))
    else:
        return HttpResponse(template.render({'text': 'reading error2'}, request))