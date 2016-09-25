#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kz-core-fast.py
#
#  Copyright 2016 Arkadiusz Ćwiek <Cwiek.Arkadiusz@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

lista_klauzul_csv = 'RawData/KlauzuleZakazane_160923.csv'

def make_rev_idx(file_name_csv):
    header=True
    kol_id=0
    kol_klauzuli=7
    separator=';'
    klauzule = open(lista_klauzul_csv).read().splitlines()

    # odczytujemy nagłówek
    i=0;
    if header:
        header = klauzule[0].split(separator)
        i=i+1
        del klauzule[0]

    # tworzymy słownik klauzul: id_klauzuli: klauzula
    klauzule_dict={}
    for row in klauzule:
        row_list = row.split(separator)
        print row_list
        try: # ValueError:
            id_klauzuli=int(row_list[kol_id])
            klauzula=row_list[kol_klauzuli]
            klauzule_dict[id_klauzuli] = klauzula
        except:
            pass

    # tworzymy odwrotny index klauzul: słowo -> (id_klauzuli (pozycje))
    idx={}
    for klauzule in klauzule_dict

    return klauzule_dict,idx




def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
