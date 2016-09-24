from openpyxl import load_workbook
from bson import json_util
import codecs
import datetime
import json

data = "klauzule_min_160923.xlsx"
out = "klauzulePython.json"

naglowki = ['lp','wyrokData','syg','sad','powod','pozwani','klauzula','wpisData','uwagi','branza']
dodatkowe = ['parent','wyszukiwanie']

def przeprocsujKlauzule(string):
    return string[1:-1]

def grabData(sheet):
    data = {}
    ii = 0
    for row in w.iter_rows(min_row=2, max_col=10, max_row=6627): # wszystkie rzedy poza naglowkami
        line = {}
        for jj,cell in enumerate(row):
            value = cell.value
            if value == None and jj ==6:
                continue
            if jj == 6: # klauzule maja zwyczaj miec " na poczatku i na koncu
                line[naglowki[jj]] = przeprocsujKlauzule(value)
                #print przeprocsujKlauzule(cell.value)
            else:
                line[naglowki[jj]] = value
                #print cell.value
            #print type(cell.value)

        line['parent'] = line['lp'] # dla kazdej bazowej klauzuli jego rodzic to numer porzadkowy na liscie
        # to sie przyda do synonimow
        line['wyszukiwanie'] = [] # wersje dla wyszukiwarki
        data[ii] = line
        ii += 1
    return data

def writeOut(data, out):
    with open(out, 'w') as f:
        json.dump(data, f, default=json_util.default)

if __name__ == "__main__":
    wb = load_workbook(filename = 'klauzule_min_160923.xlsx')
    w = wb[wb.get_sheet_names()[0]]
    data = grabData(w)
    writeOut(data, out)
