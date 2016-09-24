from pyPdf import PdfFileReader

def handle_uploaded_text_file(f):
    result = ""
    for chunk in f.chunks():
        result += (chunk + "<br />")
    return result

def handle_uploaded_pdf_file(f):
    # with open('name2.pdf', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    ff = open('name2.pdf', 'rb')
    reader = PdfFileReader(ff)
    contents = ''
    for i in range(reader.numPages):
        contents += reader.getPage(i).extractText()
    ff.close()
    return contents