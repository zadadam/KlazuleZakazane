from pyPdf import PdfFileReader

def handle_uploaded_text_file(f):
    result = ""
    for chunk in f.chunks():
        result += (chunk + "<br />")
    return result

def handle_uploaded_pdf_file(f):
    reader = PdfFileReader(f)
    contents = ''
    for i in range(reader.numPages):
        contents += reader.getPage(i).extractText()
    f.close()
    return contents