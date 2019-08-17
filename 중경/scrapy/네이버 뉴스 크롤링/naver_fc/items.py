# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverFcItem(scrapy.Item):
    url = scrapy.Field()
    # author= scrapy.Field()
    date= scrapy.Field()
    title= scrapy.Field()
    content= scrapy.Field()
    name = scrapy.Field()