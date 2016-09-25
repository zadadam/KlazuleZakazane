from django.http import HttpResponse
from django.template import loader
from .helper import handle_uploaded_text_file, handle_uploaded_pdf_file


def index(request):
    if request.method == 'POST':
        return handlePost(request)
    else:
        template = loader.get_template('Website/index.html')
        return HttpResponse(template.render({'text': ''}, request))

def handlePost(request):
    template = loader.get_template('Website/index.html')
    if request.FILES == {}:
        agreementContent = request.POST.get('pastedAgreement')
    else:
        f = request.FILES['fileToUpload']
        if f.name[-3:] == "pdf":
            agreementContent = handle_uploaded_pdf_file(f)
        else:
            agreementContent = handle_uploaded_text_file(f)
    results = getResults(agreementContent)
    return HttpResponse(template.render({'agreementContent': agreementContent, 'probability': 80, 'results': results}, request))

def info(request):
    template = loader.get_template('Website/info.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('Website/contact.html')
    return HttpResponse(template.render({}, request))

def getResults(str):
    return [
        {'umowa':'Fragment umowy, fragment umowy, Fragment umowy, fragment um owy, Fragment umowy, fragment umowy,Fragment umowy, fragment umowy',
         'klauzula': 'klauzula, klauzula, klauzula',
         'odnosnik': 'odnosnik'},
        {'umowa': 'Fragment umowy2, fragment umowy2',
          'klauzula': 'klauzula3, klauzula2, klauzula2',
          'odnosnik': 'odnosnik4'}
    ]