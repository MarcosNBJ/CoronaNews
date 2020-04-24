# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose


class CoronaNewsItem(scrapy.Item):

    title = scrapy.Field(input_processor=MapCompose(
        str.strip), output_processor=TakeFirst())

    thumbnail_url = scrapy.Field(output_processor=TakeFirst())