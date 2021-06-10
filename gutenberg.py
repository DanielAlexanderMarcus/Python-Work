from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from collections import Counter




def search_documents(word, limit):
    dict = {}
    docid = 100
    iterator = 0
    while docid >= 1:
        try:
            text = strip_headers(load_etext(docid)).strip()
            text = text.split()
            for i in text:
                if i == word:
                    iterator = iterator+1
            dict[docid] = iterator
            docid = docid-1
            iterator = 0
        except:
            print('docid '+ str(docid) + ' has no book available')
            docid = docid - 1
    my_keys = sorted(dict, key=dict.get, reverse=True)[:limit]
    #print(dict)
    print(my_keys)
    return my_keys


def search_words(docid, limit):
    lst = []
    try:
        text = strip_headers(load_etext(docid)).strip()
        text = text.split()
        lst.extend(text)
        my_keys = sorted(dict(Counter(lst)), key=dict(Counter(lst)).get, reverse=True)[:limit]
    except:
        print('docid ' + str(docid) + ' has no book available')
        return None
    print(my_keys)
    return my_keys




search_documents('house', 10)
search_words(39, 10)
