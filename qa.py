# -*- coding: utf-8 -*-

import urllib
import lxml.html

def QuoraLinkSpider(adress):
    page = urllib.urlopen(adress)
    finPage = page.read()
    
    doc = lxml.html.document_fromstring(finPage.decode('utf-8'))

    list_of_urls = []
    for question in doc.cssselect('.question_link'):
        list_of_urls.append(question.get('href'))
    
    for url in list_of_urls:
        return url

QuoraLinkSpider('file:///home/fedor/Dropbox/Science/qa_spider/saved_pages/New%20Questions%20-%20Quora.html') #Сюда кидаем адрес страницы
