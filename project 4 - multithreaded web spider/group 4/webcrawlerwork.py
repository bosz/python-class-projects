import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://www.localhost/dashboard/"
urls = [url]

if len(url) > 0 :
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext, "lxml")

	urls.pop(0)

	for tag in soup.findAll('a', href=True):

		print tag
