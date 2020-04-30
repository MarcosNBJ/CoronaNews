# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class G1Item(scrapy.Item):
    '''
    Items for G1 scrapper
    '''

    # using strip to get rid of blank spaces and new lines in title
    title = scrapy.Field(input_processor=MapCompose(
        str.strip), output_processor=TakeFirst())

    thumbnail_url = scrapy.Field(output_processor=TakeFirst())
    source_url = scrapy.Field(output_processor=TakeFirst())


class TerraItem(scrapy.Item):

    # using join because the field is returned as list
    title = scrapy.Field(output_processor=Join())
    thumbnail_url = scrapy.Field(output_processor=TakeFirst())
    source_url = scrapy.Field(output_processor=TakeFirst())
