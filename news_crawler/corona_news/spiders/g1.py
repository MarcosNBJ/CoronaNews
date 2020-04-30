# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from ..items import G1Item


class G1Spider(scrapy.Spider):
    '''
    Spider responsible for scrapping data from Globo's G1 site
    '''
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    region = ''

    def start_requests(self):

        # choosing region by received parammeter
        yield scrapy.Request(url=f'https://g1.globo.com/busca/?q=coronavirus+{self.region}&page=1',
                             callback=self.parse)

    def parse(self, response):
        """This function gathers title, thumbnail, and source url of all news found by the search.

        @url https://g1.globo.com/busca/?q=coronavirus+DF&page=1
        @returns items 1
        @scrapes title thumbnail_url source_url
        """

        news = response.xpath(
            ".//li[@class='widget widget--card widget--info']")
        for new in news:
            loader = ItemLoader(item=G1Item(),
                                selector=new, response=response)
            loader.add_xpath(
                "title", ".//div/a/div[@class='widget--info__title product-color ']/text()")
            loader.add_xpath(
                "thumbnail_url", "div[@class='widget--info__media-container ']/a/img/@src")
            loader.add_xpath(
                "source_url", ".//div/a/@href"
            )

            yield loader.load_item()

        # pagination handling
        next_page = response.urljoin(response.xpath(
            "//div[@class='pagination widget']/a/@href").get())
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )
