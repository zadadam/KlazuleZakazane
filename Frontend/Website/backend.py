#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def make_rev_idx(file_name_csv):
    header=True
    kol_id=0
    kol_org = 6
    kol_klauzuli=-1
    separator=";"
    #klauzule = open(file_name_csv).read().splitlines()
    klauzule = codecs.open(file_name_csv, "r", "utf-8").readlines()
    #print type(klauzule[0])

    i=0;
    if header:
        header = klauzule[0].split(separator)
        i=i+1
        del klauzule[0]

    klauzule_dict={}
    klauzule_org={}
    for row in klauzule:
        row_list = row.split(separator)
#         print row_list
        try: # ValueError:
            id_klauzuli=int(row_list[kol_id])
            klauzula=row_list[kol_klauzuli]
            klauzula_org = row_list[kol_org]
            klauzule_dict[id_klauzuli] = klauzula
            klauzule_org[id_klauzuli] = klauzula_org
        except:
            pass
    return klauzule_dict, klauzule_org

#dane_klauzul = make_rev_idx(u"/Users/Marcin/dane_hackaton/KlazuleZakazane/RawData/out.csv")
dane_klauzul, dane_org = make_rev_idx(u"../RawData/out.csv")


import numpy as np

def crawly(umowa, klauzula, threshold):
   if (len(umowa) <= len(klauzula)):
       return (-1, -1)
   i, j , k, um_length, kl_length, counter = 0, 0, 0, len(umowa), len(klauzula), 0
   while (i < um_length):
       if (umowa[i]==klauzula[0]):
           k = i
           while (counter <= threshold and i + 1 < um_length):
               while ((umowa[i]==klauzula[j]) & (j + 1 < kl_length) & (i + 1 < um_length)):
                   j += 1
                   i += 1
               counter += 1
               i += 1
           if (j == kl_length - 1):
               return (i + 1 - kl_length - counter, i )# + counter)
           else:
               i = k + 1
               j = 0
               counter = 0
       else:
           i += 1
   return -1, -1

def unordered_crawly(umowa, klauzula, threshold):

    klauzula_tmp = list(klauzula)

    if (len(umowa) <= len(klauzula)):
        return -1, -1
    i, j , k, um_length, kl_length, counter = 0, 0, 0, len(umowa), len(klauzula), 0

    while (i < um_length):
        if (umowa[i] in klauzula_tmp):
            k = i
            while ((counter < threshold) & (i < um_length + 1)):
                while ((umowa[i] in klauzula_tmp) & (j + 1 < kl_length) & (i + 1 < um_length)):
                    klauzula_tmp.remove(umowa[i])
                    j += 1
                    i += 1
                counter += 1
                i += 1
            if (j == kl_length - 1):
                return (i + 1 - kl_length - counter, i)
            else:
                klauzula_tmp = klauzula
                i = k + 1
                j = 0
                counter = 0
        else:
            i += 1
    return -1, -1

def odpalSzukanie(umowa_org, precyzja):
    umowa = umowa_org.split()
    odpowiedz = []
    for id_klauzula, klauzula in dane_klauzul.iteritems():
        klauzula_temp = klauzula.split()
        result, end_poz = unordered_crawly(umowa, klauzula_temp, precyzja)
        # print result
        if (result > -1):
            frg_umowy = umowa[result:end_poz]
            odpowiedz.append({"umowa": " ".join(frg_umowy), "klauzula":dane_org[id_klauzula], "odnosnik":""})
    #[{umowa: "", klauzula:"",odnosnik"" }]
    return odpowiedz
