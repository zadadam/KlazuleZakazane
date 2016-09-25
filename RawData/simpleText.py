# -*- coding: utf-8 -*-

import sys

u'ąĄęĘłŁóÓźŹżŻńŃśŚćĆ'
pol2eng = {
    u'\u0105' :'a',
    u'\u0104' :'A',
    u'\u0119' :'e',
    u'\u0118' :'E',
    u'\u0142' :'l',
    u'\u0141' :'L',
    u'\xf3' :'o',
    u'\xd3' :'O',
    u'\u017a' :'z',
    u'\u0179' :'Z',
    u'\u017c' :'z',
    u'\u017b' :'Z',
    u'\u0144' :'n',
    u'\u0143' :'N',
    u'\u015b' :'s',
    u'\u015a' :'S',
    u'\u0107' :'c',
    u'\u0106' :'S',
    u'\u2013' :'-',
    u'\xa7' : 's', # pownien byc znak paragrafu
    u'\u201d' : 'e',
    u'\u201D' : '"',
    u'\u201e' : '"',
    u'\u2026' : '...',
}

def replacePol(text):
    for kk in pol2eng.keys():
        text2 = text.replace(kk, pol2eng[kk])
        text = text2
    text3 = ''.join([i if ord(i) < 128 else ' ' for i in text])
    return str(text3)

if __name__ == "__main__":
    test = u'Za żółć gęślą jaźń'
    replacePol(test)
