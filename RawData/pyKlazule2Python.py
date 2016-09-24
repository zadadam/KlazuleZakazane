from openpyxl import load_workbook
from bson import json_util
import codecs
import datetime
import json
import re

data = "klauzule_min_160923.xlsx"
out = "klauzulePython.json"

naglowki = ['lp','wyrokData','syg','sad','powod','pozwani','klauzula','wpisData','uwagi','branza']
dodatkowe = ['parent','wyszukiwanie','saos']

def przeprocesujKlauzule(string):
    return string[1:-1]

def sygnaturaAktDlaSAOS(syg):
    """zwracana krotka: <rzymskie> <kodSadu> <numer>/<rok>"""
    pattern = r'(\w+) (\w+)\s*(\d+)/(\d+)'
    m = re.findall(pattern, syg, re.LOCALE)
    saos = ()
    if m:
        saos = m[0]
        #print saos
    else:
        print "WARNING!!!"
        print syg
        pass
    return saos


def wersjeDoWyszukiwania(tekst):
    wersje = {}
    wersje['wprost'] = tekst

    # teraz robimy uzmiennienie ze wzgledu na (...)
    protrojneKropki = (tekst.replace('(...)', '*')).replace('...','*')
    wersje['kropki'] = protrojneKropki
    #print wersje
    return wersje

def znajdzGwiazdki(tekst):
    print tekst.count(u'...')
    print tekst.count(u'...')

def grabData(sheet):
    data = {}
    ii = 0
    for row in w.iter_rows(min_row=2, max_col=10, max_row=6627): # wszystkie rzedy poza naglowkami
        line = {}
        skipRow = False
        for jj,cell in enumerate(row):
            value = cell.value
            if value == None and jj ==6: # ta linia mowi o tym, ze nie mamy naglowka
                skipRow = True
                break
            if jj == 6: # klauzule maja zwyczaj miec " na poczatku i na koncu
                line[naglowki[jj]] = przeprocesujKlauzule(value)
                #print przeprocsujKlauzule(cell.value)
            else:
                line[naglowki[jj]] = value
                #print cell.value
            #print type(cell.value)
        if skipRow: # musimy wyskoczyc z dwoch petli
            continue

        line['parent'] = line['lp'] # dla kazdej bazowej klauzuli jego rodzic to numer porzadkowy na liscie
        # to sie przyda do synonimow
        line['wyszukiwanie'] = wersjeDoWyszukiwania(line['klauzula']) # wersje dla wyszukiwarki
        line['saos'] = sygnaturaAktDlaSAOS(line['syg'])
        if not line['saos']:
            print line['lp']
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
