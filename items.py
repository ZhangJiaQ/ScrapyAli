# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


class AlispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AliSpiderInfoItem(scrapy.Item):
    company_name = scrapy.Field(
        input_processor=MapCompose()
    )
    phone_num = scrapy.Field()
    address = scrapy.Field()
    company_url = scrapy.Field()

