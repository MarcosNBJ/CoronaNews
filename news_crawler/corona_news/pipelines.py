# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CoronaNewsPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'g1':
            item.setdefault(
                'thumbnail_url', 'https://s.glbimg.com/jo/g1/static/live/imagens/img_facebook.png')
        else:
            item.setdefault(
                'thumbnail_url', 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSjeVH58qf1QYfN7qR8J0IQro_NcRM2FBwoCZ58WXJXldSSOZcSNxPwmgF7')

        return item
