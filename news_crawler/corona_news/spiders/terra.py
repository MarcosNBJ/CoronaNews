# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy_selenium import SeleniumRequest
from scrapy.loader import ItemLoader
from ..items import TerraItem


class TerraSpider(scrapy.Spider):
    '''
    Spider responsible for scrapping data from Terra's site
    '''

    name = 'terra'
    region = ''

    def start_requests(self):
        yield SeleniumRequest(

            # choosing region by parameter
            url=f'https://www.terra.com.br/busca/?q=coronavirus%20{self.region}',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        """This function gathers title, thumbnail, and source url of all news found by the search.

        """
        driver = response.request.meta["driver"]

        # loop for pagination handling
        for i in range(1, 11):

            # on the first page we can execute the xpath directly on the response, without scrolling
            if i == 1:
                products = response.xpath(
                    "//div[@class='gsc-expansionArea']/div[contains(@class, 'gsc-result')]")

            # else, we need to scroll down and click on next page, aplying xpath on the selenium driver
            else:
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
