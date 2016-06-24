import threading, urllib, urlparse
from HTMLParser import HTMLParser
import sys

class LinkHTMLParser(HTMLParser):
      A_TAG = "a"
      HREF_ATTRIBUTE = "href"

      def __init__(self):
      	  self.links = []
	  HTMLParser.__init__(self)
		
      def handle_starttag(self, tag, attrs):
      	  """Add all 'href' links within 'a' tags to self.links"""
      	  if cmp(tag, self.A_TAG) == 0:
	     for (key, value) in attrs:
       	     	 if cmp(key, self.HREF_ATTRIBUTE) == 0:
		    self.links.append(value)

      def handle_endtag(self, tag):
      	  pass       


class CrawlerThread(threading.Thread):
      def __init__(self, binarySemaphore, url, crawlDepth):
      	  self.binarySemaphore = binarySemaphore
	  self.url = url
	  self.crawlDepth = crawlDepth
	  self.threadId = hash(self)
	  threading.Thread.__init__(self)

      def run(self):
      	  """Print out all of the links on the given url associated with this particular thread. Grab the passed in 
	  binary semaphore when attempting to write to STDOUT so that there is no overlap between threads' output."""
	  socket = urllib.urlopen(self.url)  
	  urlMarkUp = socket.read()
	  linkHTMLParser = LinkHTMLParser()
	  linkHTMLParser.feed(urlMarkUp)
      	  self.binarySemaphore.acquire() # wait if another thread has acquired and not yet released binary semaphore
	  print "Thread #%d: Reading from %s" %(self.threadId, self.url)
	  print "Thread #%d: Crawl Depth = %d" %(self.threadId, self.crawlDepth)
      	  print "Thread #%d: Retreived the following links..." %(self.threadId)
	  urls = []
	  for link in linkHTMLParser.links:
	      link = urlparse.urljoin(self.url, link)
	      urls.append(link)
	      print "\t"+link
	  print "" 
	  self.binarySemaphore.release()	     
	  for url in urls:
	      # Keep crawling to different urls until the crawl depth is less than 1
              if self.crawlDepth > 1:
	      	 CrawlerThread(binarySemaphore, url, self.crawlDepth-1).start()		 
      

	  
if __name__ == "__main__":   
   binarySemaphore = threading.Semaphore(1)
   urls = [("http://www.google.com", 1), ("http://www.twitter.com", 2), ("http://www.facebook.com", 1), ("http://www.cnn.com", 1), 
   	   ("http://www.nyt.com", 1), ("http://www.schwab.com", 1), ("http://www.bankofamerica.com", 1)]
   for (url, crawlDepth) in urls:
       CrawlerThread(binarySemaphore, url, crawlDepth).start()