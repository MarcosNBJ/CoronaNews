# -*- coding: utf-8 -*-

import scrapy


class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/busca/?q=coronavirus+df&page=1']

    def parse(self, response):
        news = response.xpath(
            ".//li[@class='widget widget--card widget--info']")
        for new in news:
            title = new.xpath(
                ".//div/a/div[@class='widget--info__title product-color ']/text()").get()
            thumbnail = new.xpath(
                "div[@class='widget--info__media-container ']/a/img/@src").get()

            yield{
                'title': title,
                'thumbnail': thumbnail
            }
        next_page = response.urljoin(response.xpath(
            "//div[@class='pagination widget']/a/@href").get())
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )
