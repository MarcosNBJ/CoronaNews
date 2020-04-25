# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy_selenium import SeleniumRequest
from scrapy.loader import ItemLoader
from ..items import TerraItem


class TerraSpider(scrapy.Spider):
    name = 'terra'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.terra.com.br/busca/?q=coronavirus%20df',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):

        products = response.xpath(
            "//div[@class='gsc-expansionArea']/div[contains(@class, 'gsc-result')]")
        for product in products:

            loader = ItemLoader(item=TerraItem(),
                                selector=product, response=response)
            loader.add_xpath(
                "title", ".//div[contains(@class, 'gs-result')]/div[@class='gsc-thumbnail-inside']/div/a//text()")
            loader.add_xpath(
                'thumbnail_url', ".//div/div[@class='gsc-table-result']/div/div/a/img/@src")
            loader.add_xpath(
                "source_url", ".//div[contains(@class, 'gs-result')]/div[@class='gsc-thumbnail-inside']/div/a/@href")
            yield loader.load_item()

        driver = response.request.meta["driver"]

        for i in range(2, 11):

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_xpath(
                f'//div[3]/div[1]/div/div/div/div[5]/div[2]/div/div/div[2]/div/div[{i}]').click()
            time.sleep(1)
            s = scrapy.Selector(text=driver.page_source)
            products = s.xpath(
                "//div[@class='gsc-expansionArea']/div[contains(@class, 'gsc-result')]")
            for product in products:
                loader = ItemLoader(item=TerraItem(),
                                    selector=product, response=response)
                loader.add_xpath(
                    "title", ".//div[contains(@class, 'gs-result')]/div[@class='gsc-thumbnail-inside']/div/a//text()")
                loader.add_xpath(
                    'thumbnail_url', ".//div/div[@class='gsc-table-result']/div/div/a/img/@src")
                loader.add_xpath(
                    "source_url", ".//div[contains(@class, 'gs-result')]/div[@class='gsc-thumbnail-inside']/div/a/@href")
            yield loader.load_item()
