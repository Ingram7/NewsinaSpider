# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class NewsinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ctime = Field()
    url = Field()
    wapurl = Field()
    title = Field()
    media_name = Field()
    keywords = Field()
    content = Field()
