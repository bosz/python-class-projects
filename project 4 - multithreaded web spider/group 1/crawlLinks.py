# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

webSiteFile = urllib2.urlopen("http://www.nukeboard.co")
webSiteHtml = webSiteFile.read()
webSiteFile.close()

soup = BeautifulSoup(webSiteHtml, "lxml")
getAllLinks = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
