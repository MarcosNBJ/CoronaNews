# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from ..items import CoronaNewsItem


class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/busca/?q=coronavirus+df&page=1']

    def parse(self, response):
        news = response.xpath(
            ".//li[@class='widget widget--card widget--info']")
        for new in news:
            loader = ItemLoader(item=CoronaNewsItem(),
                                selector=new, response=response)
            loader.add_xpath(
                "title", ".//div/a/div[@class='widget--info__title product-color ']/text()")
            loader.add_xpath(
                "thumbnail_url", "div[@class='widget--info__media-container ']/a/img/@src")

            yield loader.load_item()

        next_page = response.urljoin(response.xpath(
            "//div[@class='pagination widget']/a/@href").get())
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )