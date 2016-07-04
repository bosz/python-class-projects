# -*- coding: utf-8 -*-
"""This file is a basic spider created on top of the BaseSpider class.

How to run:
    scrapy runspider SpiderMultithreaded.py
    
"""
from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.spider import BaseSpider


class Item(Item):
    # Items are defined in a declarative style. If you attempt to store a field
    # not defined here, an exception will be raised.
    title = Field()
    content = Field()
    links = Field()
    url = Field()


class SpiderMultithreaded(BaseSpider):
    """This spider crawls the website efarm.dev."""
    # The name is the unique identifier for this spider.
    name = 'SpiderMultithreaded'
    # These URLs are the initial requests performed by the spider.
    start_urls = [
        'http://efarm.dev',
    ]

    # The default callback for the start urls is `parse`.
    # This method must return either items or requests.
    def parse(self, response):
        # Instance selector in order to query the html document.
        sel = Selector(response)
        # Instance our item. The item class have a dict-like interface.
        item = Item()
        # The method `extract()` always returns a list. So we extract the
        # first value with [0]. This is not needed when using the item loaders.
        # We can use a XPath rule to extract information from the html.
        item['title'] = sel.xpath('//h1/text()').extract()[0:]
        # Or we can use a CSS expression as well.
        item['content'] = sel.css('p::text').extract()[0:]
        item['links'] = sel.xpath('//a/text()').extract()[0:]
        item['url'] = response.url
        # Finally return the scraped item.
        return item