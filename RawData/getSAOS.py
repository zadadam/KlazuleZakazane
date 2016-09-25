# -*- coding: utf-8 -*-

def getSOASjQuery(tom, sad, numer, rok):
    """wszystko ma byc stringami"""
    urlTemplate = "https://www.saos.org.pl/search?signature=%s&all=%s&size=20&sort=JUDGMENT_DATE%%2Cdesc"
    textSearch = "%s+%s+%s%%2F%s" % (tom, sad, numer, rok)
    url = urlTemplate % (textSearch, textSearch)
    return url

if __name__ == "__main__":
    print getSOASjQuery('VI', 'ACa', '1114', '13')
    pass
